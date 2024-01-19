# Import des bibliothèques nécessaires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Étape 1 : Charger les données avec Pandas
df = pd.read_excel("points.xlsx")
X = df.values  # Construire le tableau Numpy des données X

# Étape 2 : Catégorisation avec K-means
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Étape 3 : Afficher la partition finale
labels = kmeans.labels_
print("Partition finale :")
print(labels)

# Étape 4 : Afficher les centres de gravité
centers = kmeans.cluster_centers_
print("Centres de gravité :")
print(centers)

# Étape 5 : Visualiser la catégorisation avec les centres de gravité
colors = ['red', 'green', 'blue']
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='X', s=200, label='Centers')
plt.title('Catégorisation avec K-means')
plt.xlabel('Axe X')
plt.ylabel('Axe Y')
plt.legend()
plt.show()

# Étape 6 : Visualiser la catégorisation avec annotation des individus
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
for i, txt in enumerate(df.index):
    plt.annotate(txt, (X[i, 0], X[i, 1]), fontsize=8, ha='right')
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='X', s=200, label='Centers')
plt.title('Catégorisation avec K-means')
plt.xlabel('Axe X')
plt.ylabel('Axe Y')
plt.legend()
plt.show()
