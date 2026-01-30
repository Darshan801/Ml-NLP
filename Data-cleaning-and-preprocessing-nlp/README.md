# Data cleaning and processing using NLP

## Project Overview
This project focuses on data cleaing and processing using Machine Learning and NLP techniques.

## Structure
- `src/` – preprocessing and supervised training notebooks
- `data/` – dataset files
- `venv/` – virtual environment (ignored)

## Technologies
- Python
- Pandas, NumPy
- re (to validate the email)
- Git & GitHub

## Results
- successfully handle missing data 
- successfully handle invalid email using re
- successgully handle invalid date 
- normalized gender 
- droped irrelevant columns
- finalized validation
- successfully saved the clean data

## How to Run
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/data-cleaning&preprocessing.ipynb