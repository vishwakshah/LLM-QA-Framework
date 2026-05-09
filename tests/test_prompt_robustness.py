from utils.llm_client import get_llm_response

def test_same_question_different_phrasing():
    prompt1 = "What is the capital of France?"
    prompt2 = "France's capital city is?"
    prompt3 = "Which city is the capital of France?"
    
    response1 = get_llm_response(prompt1)
    response2 = get_llm_response(prompt2)
    response3 = get_llm_response(prompt3)
    
    print(f"\nResponse 1: {response1}")
    print(f"Response 2: {response2}")
    print(f"Response 3: {response3}")
    
    assert "Paris" in response1, f"Failed for prompt 1: {response1}"
    assert "Paris" in response2, f"Failed for prompt 2: {response2}"
    assert "Paris" in response3, f"Failed for prompt 3: {response3}"

def test_uppercase_lowercase():
    prompt1 = "what is the capital of japan?"
    prompt2 = "WHAT IS THE CAPITAL OF JAPAN?"
    prompt3 = "What Is The Capital Of Japan?"
    
    response1 = get_llm_response(prompt1)
    response2 = get_llm_response(prompt2)
    response3 = get_llm_response(prompt3)
    
    print(f"\nResponse 1: {response1}")
    print(f"Response 2: {response2}")
    print(f"Response 3: {response3}")
    
    assert "Tokyo" in response1, f"Failed for lowercase: {response1}"
    assert "Tokyo" in response2, f"Failed for uppercase: {response2}"
    assert "Tokyo" in response3, f"Failed for mixed case: {response3}"
