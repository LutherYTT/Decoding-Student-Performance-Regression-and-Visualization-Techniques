import pandas as pd
from sklearn.linear_model import LinearRegression

# Train a simple linear regression model.
def train_linear_model(df, features, target):
    X = df[features]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    return model

# Evaluate the model and return the score.
def evaluate_model(model, df, features, target):
    X = df[features]
    y = df[target]
    score = model.score(X, y)
    return score