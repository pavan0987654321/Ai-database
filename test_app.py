
from langchain_helper import get_few_shot_db_chain

def test_chain():
    print("Initializing Chain...")
    try:
        chain = get_few_shot_db_chain()
        print("Chain intialized.")
        
        question = "How many t-shirts do we have left for Nike in XS size and white color?"
        print(f"Asking: {question}")
        
        response = chain.run(question)
        print("Response received:")
        print(response)
        with open("test_result.txt", "w") as f:
            f.write(f"Question: {question}\n")
            f.write(f"Answer: {response}\n")
        
    except Exception as e:
        print(f"Test Failed with error: {e}")
        with open("test_error.txt", "w") as f:
            f.write(str(e))
            import traceback
            traceback.print_exc(file=f)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_chain()
