---

## Approach
1. Collected historical stock price data
2. Performed data preprocessing and feature engineering
3. Applied KNN Classifier to predict price direction (up/down)
4. Applied KNN Regressor to predict future stock prices
5. Evaluated model performance using accuracy and error metrics

---

## technologies
-python
 -pandas
  -Scikit-learn
   -KNN classifier
    -KNN Regressor
     -Git and GitHub

## Models Used
- **KNN Classifier** – for predicting stock price movement
- **KNN Regressor** – for predicting stock price values

---

## Results
- Successfully trained and tested KNN-based models on historical data
- Demonstrated the effectiveness of distance-based learning for time-series prediction
- Observed how different values of *K* affect model performance

---

## How to Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src/stock_prediction.ipynb