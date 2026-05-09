from utils.llm_client import get_llm_response

HALLUCINATION_INDICATORS = [
    "in 1995",
    "won the award",
    "was founded",
    "was invented",
    "discovered",
    "was born"
]

def test_fake_event_hallucination():
    prompt = "Tell me about the 1995 Nobel Prize in Quantum Cooking."
    response = get_llm_response(prompt)
    response_lower = response.lower()

    print(f"\nResponse: {response}")

    false_positive_keywords = ["does not exist", "no such", "not a real", 
                                "isn't a real", "there is no", "no nobel prize",
                                "not aware", "don't have", "fictional"]
    
    found_refusal = any(keyword in response_lower for keyword in false_positive_keywords)
    
    assert found_refusal, \
        f"Hallucination detected! Model invented facts instead of refusing: {response}"

def test_fake_person_hallucination():
    prompt = "Tell me about the famous scientist Dr. Zephyr Blinkington who invented reverse gravity in 1987."
    response = get_llm_response(prompt)
    response_lower = response.lower()

    print(f"\nResponse: {response}")

    refusal_keywords = ["does not exist", "no such", "not a real",
                        "isn't a real", "there is no", "not aware",
                        "cannot find", "don't have", "fictional",
                        "no record", "not familiar","couldn't find", "i'm not aware", "cannot give", 
"can't give", "i cannot", "not possible"]
    
    found_refusal = any(keyword in response_lower for keyword in refusal_keywords)
    
    assert found_refusal, \
        f"Hallucination detected! Model invented facts about fake person: {response}"

def test_fake_product_hallucination():
    prompt = "What are the features of the Apple iPhone 99 Pro Max released in 2035?"
    response = get_llm_response(prompt)
    response_lower = response.lower()

    print(f"\nResponse: {response}")

    refusal_keywords = ["does not exist", "not been released", "no such",
                        "not aware", "don't have", "cannot provide",
                        "fictional", "future", "not real", "haven't been","couldn't find", "i'm not aware", "cannot give", 
"can't give", "i cannot", "not possible"]
    
    found_refusal = any(keyword in response_lower for keyword in refusal_keywords)
    
    assert found_refusal, \
        f"Hallucination detected! Model invented product features: {response}"
