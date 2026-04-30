import pandas as pd

data = {
    'income': [40000,60000,50000,80000,90000,30000,70000,65000,52000,85000],
    'spending': [60,40,55,30,20,70,35,45,65,25],
    'age': [25,34,28,45,52,23,40,36,29,48]
}

df = pd.DataFrame(data)
df.to_csv("customers_seg.csv", index=False)

print("customers_seg.csv created")
import pandas as pd
import matplotlib.pyplot as mtp
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("customers_seg.csv")

x = df.values

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

wcss = []

for i in range(2,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x_scaled)
    wcss.append(kmeans.inertia_)

mtp.plot(range(2,11), wcss)
mtp.title("Elbow Method")
mtp.xlabel("K")
mtp.ylabel("WCSS")
mtp.show()

kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
y = kmeans.fit_predict(x_scaled)

df['cluster'] = y

print(df)

mtp.scatter(x[y==0,0], x[y==0,1])
mtp.scatter(x[y==1,0], x[y==1,1])
mtp.scatter(x[y==2,0], x[y==2,1])

mtp.xlabel("Income")
mtp.ylabel("Spending")
mtp.title("Clusters")
mtp.show()
