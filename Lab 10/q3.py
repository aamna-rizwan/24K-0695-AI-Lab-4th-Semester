#task3
import pandas as pd

data = {
    'spending': [5000, 2000, 8000, 1500, 9000, 3000, 7000, 1200, 8500, 2500],
    'age': [25, 40, 30, 50, 28, 35, 32, 45, 29, 38],
    'visits': [20, 10, 25, 5, 30, 12, 22, 4, 28, 9],
    'frequency': [5, 2, 6, 1, 7, 3, 5, 1, 6, 2],
    'label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
df.to_csv("customers.csv", index=False)

print("customers.csv created")

#task3
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("customers.csv")

data = data.dropna()

X = data[['spending', 'age', 'visits', 'frequency']]
y = data['label']

scaler = StandardScaler()
X = scaler.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svm = SVC(kernel='linear')
svm.fit(x_train, y_train)

y_pred_svm = svm.predict(x_test)

print("SVM Accuracy:", accuracy_score(y_test, y_pred_svm))

DT = DecisionTreeClassifier()
DT.fit(x_train, y_train)

y_pred_dt = DT.predict(x_test)

print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred_dt))
