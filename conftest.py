from utils.llm_client import get_llm_response

def test_groq_connection():
    response = get_llm_response("Say hello in one word")
    print(f"\nGroq Response: {response}")
    assert response is not None
    assert len(response) > 0