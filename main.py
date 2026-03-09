from rag.retrieve import retrieve_logs
from llm.load_model import load_llm

def main():
    llm = load_llm()

    print("📞 Telecom Call-Drop Analysis Chatbot")
    print("Type 'exit' to quit\n")

    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("Bot: Goodbye 👋")
            break

        logs = retrieve_logs(query)

        prompt = f"""
        You are a telecom network expert.

        Based on the following telecom logs, answer the user's question clearly.

        Logs:
        {logs}

        Question:
        {query}

        Answer:
        """

        response = llm(prompt)
        print("\nBot:", response, "\n")

if __name__ == "__main__":
    main()
