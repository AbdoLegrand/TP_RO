import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Lecture et traitement des données
df = pd.read_excel("points.xlsx")

# Viualisation du nuage des points
fig, ax = plt.subplots()
ax.scatter(..., ..., color = 'c')
ax.set_title('...')
plt.show()

m = 3
kmeans = KMeans(n_clusters=m, random_state=0).fit(X)

# Viualisation du nuage des points
color_classe = ['g','r','b','y','c']
color_individu = []
for i in range(n):
      color_individu.append(...)
fig, ax = plt.subplots()
ax.scatter(..., ..., color = ...)
for k in range(m):
    ax.annotate('G'+str(k+1), (... ,...), fontsize=15, c='...')
ax.set_title('Les classes en couleur')
plt.show()
