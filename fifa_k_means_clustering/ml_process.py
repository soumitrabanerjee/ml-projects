import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from IPython.display import clear_output


# The selected function random_centroids generates k random centroids from the input DataFrame data.
# For each centroid,
#   it samples one value from each column (using x.sample()),
#   converts it to float, and collects these into a Series.
# All centroids are then concatenated into a new DataFrame with centroids as columns.
# This is typically used to initialize centroids for k-means clustering.

def random_centroids(data, k):
    centroids = []
    for i in range(k):
        centroid = data.apply(lambda x: float(x.sample()))
        print(centroid)
        centroids.append(centroid)
    return pd.concat(centroids, axis=1)

def get_labels(centroids, data):
    distances = centroids.apply(lambda x: np.sqrt(((data - x) ** 2).sum(axis=1)))
    labels = distances.idxmin(axis=1)
    return labels
def new_centroids(labels, data, k):
    return data.groupby(labels).apply(lambda x: np.exp(np.log(x).mean())).T

def plot_cluster(data, labels, centroids, iteration):
    pca = PCA(n_components=2)
    data2d = pca.fit_transform(data)
    centroids2d = pca.transform(centroids.T)
    clear_output(wait=True)
    plt.title(f'Iteration {iteration}')
    plt.scatter(x = data2d[:,0], y = data2d[:,1], c=labels)
    plt.scatter(x=centroids2d[:, 0], y=centroids2d[:, 1])
    plt.show()

def ml_process(data):
    data = (data - data.min()) / (data.max() - data.min()) * 9 + 1
    print("Scaled Data Description:")
    description = data.describe()
    print(description)
    print("centroids")
    centroids = random_centroids(data, 5)
    print("printing centroids")
    print(centroids)
    np.sqrt(((data - centroids.iloc[:, 0]) ** 2).sum(axis=1))
    labels = get_labels(centroids, data)
    print(labels.value_counts())
    new_centroids(labels, data, 3)
    max_iteration = 10
    k = 3
    centroids = random_centroids(data, k)
    old_centroids = pd.DataFrame
    iteration = 1
    while(iteration < max_iteration and not centroids.equals(old_centroids)):
        old_centroids = centroids
        labels = get_labels(centroids, data)
        centroids = new_centroids(labels, data, k)
        plot_cluster(data, labels, centroids, iteration)
        iteration += 1

