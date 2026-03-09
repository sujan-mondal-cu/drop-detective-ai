import streamlit as st
from agents.agent import create_agent

st.title("📡 Agent-Based Call Drop Analysis")

agent = create_agent()

query = st.text_input("Enter telecom issue:")

if st.button("Analyze"):
    with st.spinner("Analyzing logs..."):
        response = agent.run(query)
    st.success("Analysis Complete")
    st.write(response)
