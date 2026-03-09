import pandas as pd
import re
from rag.retrieve import retrieve_logs
from llm.load_model import load_llm

# Load telecom dataset
df = pd.read_csv("data/raw/telecom_logs.csv")

regions = df["Region"].unique()


def analyze_query(query):

    query_lower = query.lower()

    # -------- WORST TOWER --------
    if "worst tower" in query_lower or "worst network performance" in query_lower:

        worst = df.loc[df["Call_Drops"].idxmax()]

        return f"""
Worst Performing Tower

Tower: {worst['Tower_ID']}
Region: {worst['Region']}
Call Drops: {worst['Call_Drops']}
Signal Strength: {worst['Signal_Strength']} dBm
Congestion: {worst['Congestion_Level']}
Handoff Failure: {worst['Handoff_Failure']} %

Cause: {worst['Notes']}
"""

    # -------- MOST STABLE REGION --------
    if "stable network" in query_lower or "most stable" in query_lower:

        stability = df.groupby("Region")["Call_Drops"].mean()

        best_region = stability.idxmin()

        return f"""
Most Stable Network Region

Region: {best_region}

Average Call Drops: {stability.min():.1f}
"""

    # -------- WEAK SIGNAL TOWERS --------
    if "weak signal" in query_lower:

        weak = df[df["Signal_Strength"] < -90]

        result = "Towers With Weak Signal\n\n"

        for _, row in weak.iterrows():
            result += f"{row['Tower_ID']} ({row['Region']}) → {row['Signal_Strength']} dBm\n"

        return result

    # -------- NETWORK HEALTH --------
    if "network health" in query_lower:

        avg_drop = df["Call_Drops"].mean()
        avg_signal = df["Signal_Strength"].mean()

        return f"""
Network Health Report

Average Call Drops: {avg_drop:.1f}
Average Signal Strength: {avg_signal:.1f} dBm
"""

    # -------- TOWER ANALYSIS --------
    match = re.search(r"T\d+", query.upper())

    if match:

        tower_id = match.group()

        tower_data = df[df["Tower_ID"] == tower_id]

        if len(tower_data) == 0:
            return "No tower data found."

        region = tower_data["Region"].iloc[0]
        drops = tower_data["Call_Drops"].mean()
        signal = tower_data["Signal_Strength"].mean()
        congestion = tower_data["Congestion_Level"].mode()[0]
        handoff = tower_data["Handoff_Failure"].max()
        notes = ", ".join(tower_data["Notes"].unique())

        return f"""
Tower Analysis

Tower: {tower_id}
Region: {region}

Average Call Drops: {drops:.1f}
Signal Strength: {signal:.1f} dBm
Congestion: {congestion}
Handoff Failure: {handoff} %

Cause: {notes}
"""

    # -------- REGION ANALYSIS --------
    for r in regions:
        if r.lower() in query_lower:

            region_data = df[df["Region"] == r]

            drops = region_data["Call_Drops"].mean()
            signal = region_data["Signal_Strength"].mean()
            congestion = region_data["Congestion_Level"].mode()[0]

            return f"""
Region Analysis

Region: {r}

Average Call Drops: {drops:.1f}
Average Signal Strength: {signal:.1f} dBm
Congestion Level: {congestion}
"""

    return None


def main():

    llm = load_llm()

    print("\n📡 Drop Detective AI")
    print("Telecom Network Log Analysis")
    print("Type 'exit' to quit\n")

    while True:

        query = input("You: ").strip()

        if query.lower() in ["exit", "quit"]:
            print("\nBot: Goodbye 👋\n")
            break

        print("\nBot is analyzing...\n")

        # First try dataset analytics
        result = analyze_query(query)

        if result:
            print("Bot:", result)
            print("-" * 50)
            continue

        # Otherwise use LLM + RAG
        logs = retrieve_logs(query)

        prompt = f"""
You are a telecom network engineer.

Based on the telecom logs answer the question.

Logs:
{logs}

Question:
{query}
"""

        response = llm.invoke(prompt)

        print("Bot:", response)
        print("-" * 50)


if __name__ == "__main__":
    main()