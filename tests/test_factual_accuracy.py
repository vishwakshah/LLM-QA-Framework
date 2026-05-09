from utils.llm_client import get_llm_response

def test_capital_of_france():
    prompt = "What is the capital of France? Answer in one word."
    response = get_llm_response(prompt)
    assert "Paris" in response, f"Expected Paris but got: {response}"
    print(f"\nResponse: {response}")

def test_who_wrote_romeo_and_juliet():
    prompt = "Who wrote Romeo and Juliet? Answer in one word."
    response = get_llm_response(prompt)
    assert "Shakespeare" in response, f"Expected Shakespeare but got: {response}"
    print(f"\nResponse: {response}")

def test_boiling_point_of_water():
    prompt = "What is the boiling point of water in Celsius? Answer in numeric digits only."
    response = get_llm_response(prompt)
    assert "100" in response, f"Expected 100 but got: {response}"
    print(f"\nResponse: {response}")
