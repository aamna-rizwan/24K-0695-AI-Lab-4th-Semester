#task 2 
import pandas as pd

data = {
    'vehicle_serial_no': [5,3,8,2,4,7,6,10,1,9],
    'mileage': [150000,120000,250000,80000,100000,220000,180000,300000,75000,280000],
    'fuel_efficiency': [15,18,10,22,20,12,16,8,24,9],
    'maintenance_cost': [5000,4000,7000,2000,3000,6500,5500,8000,1500,7500],
    'vehicle_type': ['SUV','Sedan','Truck','Hatchback','Sedan','Truck','SUV','Truck','Hatchback','SUV']
}

df = pd.DataFrame(data)
df.to_csv("vehicles.csv", index=False)

print("vehicles.csv created")

import numpy as nm
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("vehicles.csv")

le = LabelEncoder()
df['vehicle_type'] = le.fit_transform(df['vehicle_type'])

x = df.iloc[:, 1:].values

kmeans1 = KMeans(n_clusters=3, init='k-means++', random_state=42)
y1 = kmeans1.fit_predict(x)

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

kmeans2 = KMeans(n_clusters=3, init='k-means++', random_state=42)
y2 = kmeans2.fit_predict(x_scaled)

print("Without Scaling:", y1)
print("With Scaling:", y2)
