import pandas as pd
import numpy as np

np.random.seed(42)

n = 200

data = {
    'amount': np.random.randint(10, 1000, n),
    'time': np.random.randint(1, 100000, n),
    'feature1': np.random.randn(n),
    'feature2': np.random.randn(n),
    'class': np.concatenate((np.zeros(180), np.ones(20)))
}

df = pd.DataFrame(data)
df.to_csv("fraud.csv", index=False)

print("fraud.csv created")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("fraud.csv")

df_majority = df[df['class']==0]
df_minority = df[df['class']==1]

df_majority = df_majority.sample(len(df_minority), random_state=42)

df_balanced = pd.concat([df_majority, df_minority])

X = df_balanced.drop('class', axis=1)
y = df_balanced['class']

scaler = StandardScaler()
X = scaler.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

lr = LogisticRegression()
lr.fit(x_train, y_train)
y_pred1 = lr.predict(x_test)

rf = RandomForestClassifier()
rf.fit(x_train, y_train)
y_pred2 = rf.predict(x_test)

print("Logistic Regression")
print("Accuracy:", accuracy_score(y_test, y_pred1))
print("Precision:", precision_score(y_test, y_pred1))
print("Recall:", recall_score(y_test, y_pred1))
print("F1:", f1_score(y_test, y_pred1))

print("Random Forest")
print("Accuracy:", accuracy_score(y_test, y_pred2))
print("Precision:", precision_score(y_test, y_pred2))
print("Recall:", recall_score(y_test, y_pred2))
print("F1:", f1_score(y_test, y_pred2))
