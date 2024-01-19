import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

# Lecture et traitement des données
df = pd.read_excel("points.xlsx")


# Clusering avec la méthode CAH
AC = AgglomerativeClustering(n_clusters=3, linkage='ward', compute_distances=True).fit(X)


# Viualisation du nuage des points
color_classe = ['g','r','b','y','c']
color_individu = []
for i in range(n):
      color_individu.append(...)
fig, ax = plt.subplots()
ax.scatter(..., ..., color = ...)
for i in range(n):
    ax.annotate(str(i), (..., ...), c='...')
plt.show()
