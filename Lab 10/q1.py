#task1
import pandas as pd

data = {
    'sqft': [2000, 1500, 2500, 1800, 2200],
    'bedrooms': [3, 2, 4, 3, 4],
    'bathrooms': [2, 1, 3, 2, 3],
    'age': [10, 5, 8, 12, 6],
    'neighborhood': ['A', 'B', 'A', 'C', 'B'],
    'price': [500000, 350000, 650000, 400000, 600000]
}

df = pd.DataFrame(data)
df.to_csv("house_data.csv", index=False)

print("CSV file created")

#task1
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("house_data.csv")

data = data.dropna()

le = LabelEncoder()
data['neighborhood'] = le.fit_transform(data['neighborhood'])

X = data[['sqft', 'bedrooms', 'bathrooms', 'age', 'neighborhood']]
y = data['price']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

LR = LinearRegression()
ModelLR = LR.fit(x_train, y_train)

PredictionLR = ModelLR.predict(x_test)

print("Predictions:", PredictionLR)

mse = mean_squared_error(y_test, PredictionLR)
r2 = r2_score(y_test, PredictionLR)

print("MSE:", mse)
print("R2 Score:", r2)

new_house = [[2000, 3, 2, 10, 1]]
predicted_price = ModelLR.predict(new_house)

print("Predicted Price:", predicted_price)
