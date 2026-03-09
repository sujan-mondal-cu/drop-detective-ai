from agents.agent import create_agent

agent = create_agent()

while True:
    query = input("\nEnter telecom query (or 'exit'): ")
    if query.lower() == "exit":
        break
    response = agent.run(query)
    print("\n--- Agent Response ---")
    print(response)
