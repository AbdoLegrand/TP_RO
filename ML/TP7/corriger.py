# import pandas as pd
# import numpy as np
# from sklearn.cluster import AgglomerativeClustering
# import matplotlib.pyplot as plt
#
# # Étape 1 : Charger les données avec Pandas
# df = pd.read_excel("points.xlsx")
# X = df.values  # Construire le tableau Numpy des données X
#
# # Étape 2 : Regroupement hiérarchique avec la méthode CAH
# n_clusters = 2
# AC = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward', compute_distances=True).fit(X)
#
# # Étape 3 : Afficher la partition finale
# labels = AC.labels_
# print("Partition finale :")
# print(labels)
#
# # Étape 4 : Afficher le regroupement hiérarchique
# print("Regroupement hiérarchique (Ward) :")
# print(AC.children_)
#
# # Étape 5 : Afficher les distances correspondantes au regroupement hiérarchique
# print("Distances correspondantes au regroupement hiérarchique :")
# print(AC.distances_)
#
# # Étape 6 : Visualiser la catégorisation sur 3 classes
# color_classes = ['g', 'r', 'b']
# colors = [color_classes[label] for label in labels]
#
# fig, ax = plt.subplots()
# ax.scatter(X[:, 0], X[:, 1], c=colors)
#
# for i, txt in enumerate(df.index):
#     ax.annotate(str(i), (X[i, 0], X[i, 1]), color=colors[i], fontsize=8, ha='right')
#
# plt.title('Classification Ascendante Hiérarchique (CAH)')
# plt.xlabel('Axe X')
# plt.ylabel('Axe Y')
# plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram

# Étape 1 : Charger les données avec Pandas
df = pd.read_excel("points.xlsx")
X = df.to_numpy()

# Étape 2 : Réaliser la classification ascendante hiérarchique
AC = AgglomerativeClustering(n_clusters=2, linkage='ward', compute_distances=True).fit(X)

# Étape 3 : Afficher la partition finale
labels = AC.labels_
print("Partition finale : ", labels)


# Étape 4 : Afficher le regroupement hiérarchique (dendrogramme)
def plot_dendrogram(model, **kwargs):
    # Créer la matrice de liaison (linkage matrix)
    linkage_matrix = np.column_stack([model.children_, model.distances_, np.ones(model.children_.shape[0])])

    # Afficher le dendrogramme
    dendrogram(linkage_matrix, **kwargs)


plt.figure(figsize=(10, 5))
plt.title('Dendrogramme de Classification Ascendante Hiérarchique')
plot_dendrogram(AC)
plt.show()

# Étape 5 : Afficher les distances correspondantes au regroupement hiérarchique
distances = AC.distances_
print("Distances correspondantes au regroupement hiérarchique : ", distances)

# Étape 6 : Visualiser la catégorisation avec annotation des individus
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.5)
for i, label in enumerate(labels):
    plt.annotate(i, (X[i, 0], X[i, 1]), textcoords="offset points", xytext=(0, 5), ha='center')
plt.title('Classification Ascendante Hiérarchique (3 classes) - Annotation des individus')
plt.xlabel('Attribut 1')
plt.ylabel('Attribut 2')
plt.show()