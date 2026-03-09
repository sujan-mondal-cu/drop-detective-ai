import streamlit as st
import pandas as pd
import re

st.set_page_config(
    page_title="Drop Detective AI",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Drop Detective AI")

df = pd.read_csv("data/raw/telecom_logs.csv")

regions = df["Region"].unique()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

query = st.chat_input("Ask about telecom network issues...")

if query:

    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):

        with st.spinner("Analyzing telecom logs..."):

            query_lower = query.lower()
            response = ""

            # ---------------- WORST TOWER ----------------
            if "worst" in query_lower and "tower" in query_lower or "worst network performance" in query_lower:

                worst = df.loc[df["Call_Drops"].idxmax()]

                response = f"""
### Worst Performing Tower

Tower: **{worst['Tower_ID']}**

Region: **{worst['Region']}**

Call Drops: {worst['Call_Drops']}

Signal Strength: {worst['Signal_Strength']} dBm

Congestion: {worst['Congestion_Level']}

Handoff Failure: {worst['Handoff_Failure']} %

Cause: {worst['Notes']}
"""

            # ---------------- MOST CALL DROPS ----------------
            elif "most call drops" in query_lower:

                tower = df.loc[df["Call_Drops"].idxmax()]

                response = f"""
### Tower With Highest Call Drops

Tower **{tower['Tower_ID']}** in **{tower['Region']}**

Call Drops: {tower['Call_Drops']}
"""

            # ---------------- HIGHEST CONGESTION ----------------
            elif "stable network" in query_lower or "most stable" in query_lower:

                stability = df.groupby("Region")["Call_Drops"].mean()

                best_region = stability.idxmin()
                best_value = stability.min()
                response = f"""
### Most Stable Network

Region: **{best_region}**

Average Call Drops: **{best_value:.1f}**

This region has the most stable network performance.
"""                

            # ---------------- HIGHEST CONGESTION ----------------
            elif "highest congestion" in query_lower:

                congested = df[df["Congestion_Level"] == "High"]

                region = congested["Region"].value_counts().idxmax()

                response = f"""
### Congestion Hotspot

Region with highest congestion: **{region}**

Suggested Action:
Deploy additional microcells and optimize traffic load balancing.
"""

            # ---------------- AVERAGE CALL DROPS ----------------
            elif "average call drops" in query_lower:

                avg_drops = df.groupby("Region")["Call_Drops"].mean()

                response = "### Average Call Drops per Region\n\n"

                for r, val in avg_drops.items():
                    response += f"- **{r}** : {val:.1f}\n"

            # ---------------- WEAK SIGNAL ----------------
            elif "weak signal" in query_lower:

                weak = df[df["Signal_Strength"] < -90]

                response = "### Towers with Weak Signal\n\n"

                for _, row in weak.iterrows():
                    response += f"- Tower **{row['Tower_ID']}** in {row['Region']} ({row['Signal_Strength']} dBm)\n"

            # ---------------- NETWORK HEALTH ----------------
            elif "network health" in query_lower:

                avg_drop = df["Call_Drops"].mean()
                avg_signal = df["Signal_Strength"].mean()

                response = f"""
### Network Health Report

Average Call Drops: {avg_drop:.1f}

Average Signal Strength: {avg_signal:.1f} dBm

Network condition appears **moderate**.
"""

            else:

                # -------- REGION DETECTION --------
                region_found = None

                for r in regions:
                    if r.lower() in query_lower:
                        region_found = r
                        break

                # -------- SIGNAL QUERY --------
                if "signal" in query_lower:

                    match = re.search(r"T\d+", query.upper())

                    if match:

                        tower_id = match.group()
                        tower_data = df[df["Tower_ID"] == tower_id]

                        if len(tower_data) > 0:

                            signal = tower_data["Signal_Strength"].mean()

                            response = f"""
### Signal Strength

Tower **{tower_id}** signal strength is **{signal:.1f} dBm**
"""

                        else:
                            response = "No tower data found."

                    else:
                        response = "Please specify a tower ID (example: T123)."

                # -------- REGION ANALYSIS --------
                elif region_found:

                    region_data = df[df["Region"] == region_found]

                    drops = region_data["Call_Drops"].mean()
                    signal = region_data["Signal_Strength"].mean()
                    congestion = region_data["Congestion_Level"].mode()[0]
                    handoff = region_data["Handoff_Failure"].max()

                    fixes = []

                    if congestion == "High":
                        fixes.append("Deploy additional microcells")

                    if signal < -90:
                        fixes.append("Improve tower coverage")

                    if handoff > 10:
                        fixes.append("Optimize handoff algorithms")

                    if len(fixes) == 0:
                        fixes.append("Network operating normally")

                    fix_text = "\n".join([f"{i+1}. {f}" for i, f in enumerate(fixes)])

                    response = f"""
### Region Analysis

**Region:** {region_found}

Average Call Drops: {drops:.1f}

Average Signal Strength: {signal:.1f} dBm

Congestion Level: {congestion}

Handoff Failure: {handoff} %

### Suggested Resolution

{fix_text}
"""

                # -------- TOWER ANALYSIS --------
                else:

                    match = re.search(r"T\d+", query.upper())

                    if match:

                        tower_id = match.group()
                        tower_data = df[df["Tower_ID"] == tower_id]

                        if len(tower_data) > 0:

                            region = tower_data["Region"].iloc[0]
                            drops = tower_data["Call_Drops"].mean()
                            signal = tower_data["Signal_Strength"].mean()
                            congestion = tower_data["Congestion_Level"].mode()[0]
                            handoff = tower_data["Handoff_Failure"].max()
                            notes = ", ".join(tower_data["Notes"].unique())

                            response = f"""
### Tower Analysis

Tower ID: {tower_id}

Region: {region}

Average Call Drops: {drops:.1f}

Signal Strength: {signal:.1f} dBm

Congestion Level: {congestion}

Handoff Failure: {handoff} %

Cause: {notes}
"""

                        else:
                            response = "No tower data found."

                    else:
                        response = "Ask about a **region** or a **tower ID (T123)**."

        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    st.stop()