# LLM Prompt Design Impact Analysis

## Overview
This project tries to  analyzes the impact of prompt design on Large Language Model (LLM) outputs by comparing basic prompts with structured prompts across multiple NLP tasks.

## Experiments Conducted
- Analyzed how prompt structure affects LLM responses
- Compared basic and structured prompts for NLP tasks
- Documented observations and insights to improve model outputs


## we are using and implementing ML through Openai model

## Machine Learning:
- model used (gpt-3.5-turbo)

## NLP Tasks
- Text summarization
- Sentiment classification
- Text rewriting

## Technologies
- Python
- Large Language Models (LLMs)
- Prompt Engineering
- OpenAI API
- Git & GitHub

## Key Learnings
- Clear instructions improve output consistency
- Prompt constraints reduce ambiguity
- Structured prompts enhance response quality


##  note NPL is applied when model (reads text , understand meaning , generated language-based output)

## the RateLimitError: 429 occurred due to API quota exhaustion. The issue was resolved by adding a mock response

## How to Run
```bash
python -m venv venv
.venv\Scripts\activate
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
python src/prompt_experiments.ipynb


