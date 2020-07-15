# Import required packages
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv('edlich-kmeans-A0.csv')
# data.head(5)

features = ['V1', 'V2', 'V3']
print(data[features].describe())

scaler = MinMaxScaler()
scaler.fit(data)
data_scaled = scaler.transform(data)

added_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(data_scaled)
    added_squared_distances.append(km.inertia_)

# plt.plot(K, added_squared_distances, 'bx-')
# plt.xlabel('k')
# plt.ylabel('Sum_of_squared_distances')
# plt.title('Elbow Method For Optimal k')
# plt.show()

# based on the plot the optimal K seems to be 5 taking the elbow-effect into account
# A) the best K is 5


X, y = make_blobs(n_samples = 100, n_features=3, centers=5)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)

plt.show()

km = KMeans(n_clusters=5)
km = km.fit(X)
labels = km.predict(X)

C = km.cluster_centers_

# prints our clustering vectors to the console
for idx,vector in enumerate(C, start=1):
    print("\nVector number {}: X={}, Y={}, Z={}" .format(idx, vector[0], vector[1], vector[2]))


# now show our centers (clustering vectors) in the 3D graph
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='.', c='#050505', s=1000)

plt.show()