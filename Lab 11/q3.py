#task3
import pandas as pd

data = {
    'student_id': [1,2,3,4,5,6,7,8,9,10],
    'GPA': [3.5,2.8,3.9,2.5,3.2,3.8,2.7,3.6,3.0,2.9],
    'study_hours': [15,8,20,5,12,18,7,16,10,9],
    'attendance_rate': [90,70,95,60,85,92,65,88,75,72]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

print("students.csv created")

import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("students.csv")

x = df[['GPA','study_hours','attendance_rate']].values

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

wcss_list = []

for i in range(1, 7):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x_scaled)
    wcss_list.append(kmeans.inertia_)

mtp.plot(range(1,7), wcss_list)
mtp.title('Elbow Method')
mtp.xlabel('K')
mtp.ylabel('WCSS')
mtp.show()

kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
y_predict = kmeans.fit_predict(x_scaled)

df['cluster'] = y_predict

print(df)

mtp.scatter(x[y_predict==0,1], x[y_predict==0,0])
mtp.scatter(x[y_predict==1,1], x[y_predict==1,0])
mtp.scatter(x[y_predict==2,1], x[y_predict==2,0])

mtp.xlabel('Study Hours')
mtp.ylabel('GPA')
mtp.title('Student Clusters')
mtp.show()
