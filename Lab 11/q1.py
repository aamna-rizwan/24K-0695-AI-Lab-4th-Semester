#task1
import pandas as pd

data = {
    'customer_id': [1,2,3,4,5,6,7,8,9,10],
    'age': [25,34,28,45,52,23,40,36,29,48],
    'income': [40000,60000,50000,80000,90000,30000,70000,65000,52000,85000],
    'spending_score': [60,40,55,30,20,70,35,45,65,25]
}

df = pd.DataFrame(data)
df.to_csv("customer_segmentation.csv", index=False)

print("customer_segmentation.csv created")

import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("customer_segmentation.csv")

x = df.iloc[:, 1:].values

kmeans1 = KMeans(n_clusters=3, init='k-means++', random_state=42)
y1 = kmeans1.fit_predict(x)

scaler = StandardScaler()
x_scaled = x.copy()
x_scaled[:,1:] = scaler.fit_transform(x[:,1:])

kmeans2 = KMeans(n_clusters=3, init='k-means++', random_state=42)
y2 = kmeans2.fit_predict(x_scaled)

print("Without Scaling:", y1)
print("With Scaling:", y2)
