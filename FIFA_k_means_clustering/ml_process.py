import pandas as pd
import numpy as np
from matplotlib import pyplot

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

def ml_process(data):
    data = (data - data.min()) / (data.max() - data.min()) * 9 + 1
    print("Scaled Data Description:")
    description = data.describe()
    print(description)
    print("centroids")
    centroids = random_centroids(data, 5)
    print("printing centroids")
    print(centroids)
