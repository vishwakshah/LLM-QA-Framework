from utils.llm_client import get_llm_response

def test_response_consistency():
    prompt = "What is 2 + 2? Answer in numeric digits only."
    
    response1 = get_llm_response(prompt)
    response2 = get_llm_response(prompt)
    response3 = get_llm_response(prompt)
    
    print(f"\nResponse 1: {response1}")
    print(f"Response 2: {response2}")
    print(f"Response 3: {response3}")
    
    assert "4" in response1, f"Response 1 wrong: {response1}"
    assert "4" in response2, f"Response 2 wrong: {response2}"
    assert "4" in response3, f"Response 3 wrong: {response3}"

def test_country_capital_consistency():
    prompt = "What is the capital of Japan? Answer in one word."
    
    response1 = get_llm_response(prompt)
    response2 = get_llm_response(prompt)
    
    print(f"\nResponse 1: {response1}")
    print(f"Response 2: {response2}")
    
    assert "Tokyo" in response1, f"Response 1 wrong: {response1}"
    assert "Tokyo" in response2, f"Response 2 wrong: {response2}"
