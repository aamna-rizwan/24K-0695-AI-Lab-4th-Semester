import pandas as pd

data = {
    'area': [1000,1500,2000,2500,1800,2200,1400,1600,2100,2300],
    'bedrooms': [2,3,4,4,3,4,2,3,4,4],
    'bathrooms': [1,2,3,3,2,3,1,2,3,3],
    'location': ['A','B','A','C','B','A','C','B','A','C'],
    'price': [200000,300000,500000,650000,400000,600000,250000,320000,520000,630000]
}

df = pd.DataFrame(data)
df.to_csv("house.csv", index=False)

print("house.csv created")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

df = pd.read_csv("house.csv")

df = df.dropna()

le = LabelEncoder()
df['location'] = le.fit_transform(df['location'])

X = df.drop('price', axis=1)
y = df['price']

scaler = StandardScaler()
X = scaler.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

lr = LinearRegression()
lr.fit(x_train, y_train)
y_pred1 = lr.predict(x_test)

dt = DecisionTreeRegressor()
dt.fit(x_train, y_train)
y_pred2 = dt.predict(x_test)

print("Linear Regression")
print("MAE:", mean_absolute_error(y_test, y_pred1))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred1)))

print("Decision Tree")
print("MAE:", mean_absolute_error(y_test, y_pred2))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred2)))

print("Actual:", list(y_test))
print("Predicted LR:", y_pred1)
print("Predicted DT:", y_pred2)
