from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st


def main():
    # Load the OpenAI API key from the environment variable
    load_dotenv()
    # check for key
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is ${OPENAI_API_KEY}")
        

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV 📈")

    user_csv = st.file_uploader("Upload a CSV file", type="csv")
    if user_csv is not None:
        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm, user_csv, verbose=True)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            st.write(f"Your question was: {user_question}")
            response = agent.run(user_question)

            st.write(response)


if __name__ == "__main__":
    main()