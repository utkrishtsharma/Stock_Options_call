#prediction_bot.py
# prediction_bot.py

import numpy as np
from sklearn.linear_model import LogisticRegression

# Example function to predict "Call" or "Put"
def predict_option(df):
    """
    Predicts whether a "Call" or "Put" option is more likely based on stock data.
    This example uses a simple logistic regression model as a placeholder.
    """

    # Prepare data (this is a simple placeholder - in a real scenario, you would use historical data)
    df['PriceChange'] = df['4. close'].diff()
    df.dropna(inplace=True)

    # Simple heuristic: If the price is increasing, suggest "Call", otherwise "Put"
    X = df[['PriceChange']].values
    y = np.where(df['PriceChange'] > 0, 1, 0)  # 1 for "Call", 0 for "Put"

    # Train a simple logistic regression model
    model = LogisticRegression()
    model.fit(X, y)

    # Predict probabilities for the latest data point
    last_price_change = X[-1].reshape(1, -1)
    probability = model.predict_proba(last_price_change)[0]

    return probability  # [put_probability, call_probability]
