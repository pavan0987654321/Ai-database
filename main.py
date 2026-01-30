import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("AtliQ T Shirts: Retail Q&A Tool 👕")

# Force fresh chain (cache removed to apply new formatting)
def get_chain():
    return get_few_shot_db_chain()

question = st.text_input("Question: ")

if question:
    chain = get_chain()
    
    with st.spinner("Thinking..."):
        try:
            # Use invoke instead of run to get proper response
            result = chain.invoke({"query": question})
            
            # Extract the answer from result
            if isinstance(result, dict):
                response = result.get('result', str(result))
            else:
                response = str(result)
        except Exception as e:
            response = f"Error: {str(e)}"

    st.header("Answer")
    st.write(response)
