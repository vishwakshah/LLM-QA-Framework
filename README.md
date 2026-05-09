# LLM-QA-Framework

A Python-based testing framework for validating Large Language Model (LLM) 
outputs built by Vishwa Shah — Senior Quality Engineer with 9+ years of 
experience in manual and AI testing.

## About This Project
This framework automates the validation of LLM responses across five 
key quality dimensions, directly based on methodologies applied in 
production at a global billion-user AI platform.

## Test Coverage

| Module | What It Tests |
|--------|--------------|
| Factual Accuracy | Validates LLM gives correct answers to known questions |
| Consistency | Ensures same question returns same answer every time |
| Prompt Robustness | Tests LLM handles different phrasings and formats correctly |
| Safety Guardrails | Verifies LLM refuses harmful and dangerous requests |
| Hallucination Detection | Checks LLM doesn't invent facts about non-existent things |

## Tech Stack
- Python 3.13
- Pytest
- Groq API (LLaMA 3.1)
- DeepEval
- pytest-html (test reporting)
- python-dotenv

## Project Structure
LLM-QA-Framework/
├── tests/
│   ├── test_factual_accuracy.py
│   ├── test_consistency.py
│   ├── test_prompt_robustness.py
│   ├── test_safety_guardrails.py
│   └── test_hallucination.py
├── utils/
│   └── llm_client.py
├── data/
├── reports/
├── conftest.py
├── requirements.txt
└── README.md

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/LLM-QA-Framework.git
cd LLM-QA-Framework
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API key**
Create a `.env` file in the root folder:
GROQ_API_KEY=your_groq_api_key_here

**5. Run all tests**
```bash
pytest tests/ -v -s
```

**6. Generate HTML report**
```bash
pytest tests/ -v -s --html=reports/report.html
```

## Test Results
13 tests | 0 Failed | 0 Errors

## Author
**Vishwa Shah**
Senior Quality Engineer | AI, LLM & Web Specialist
vish.shah92@gmail.com