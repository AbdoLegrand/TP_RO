import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lecture et traitement des données
# 1. Utilisez la bibliothèque Pandas pour lire le data frame qui se trouve dans un fichier Excel points.xlsx.

df = pd.read_excel("points.xlsx")

# 2. Construisez le tableau Numpy des données X.
X = np.array(df)
n, p = X.shape
m = 3
print(n, p)
# 3. Générez aléatoirement 3 centres initiaux en ajoutant des réalisations de la loi Normale centrée réduite aux composantes du centre de gravité du nuage des points.

G = np.mean(X,axis=0)
centres = np.zeros((m,p))
for k in range(m):
    centres[k,:] = G + np.random.randn(1,p)

# Viualisation du nuage des points au début
# np.describe()
# 4. Visualisez le nuage de points et les centres initiaux avec Matplotlib.
color_classe = ['g','r','b','y','c']
fig, ax = plt.subplots()
ax.set_title('Le début ')
ax.scatter(X[:,0], X[:,1], color = 'y')
for k in range(m):
    ax.annotate('G'+str(k+1), (centres[k,0], centres[k,1]), fontsize=20, c='k')
# plt.show()

# Apprentissage
# 5. Calculez l’inertie totale de ce nuage de points. Remarquez qu’elle est égale à l’inertie intra avant la catégorisation des individus dans des classes différentes.

Y = np.zeros(n).reshape(n,1)
Inertie_totale = np.sum([np.power(X[i,:]-G,2) for i in range(n)])/n
print("Inertie totale : ",Inertie_totale)
new_I_intra = Inertie_totale
amelioration = True
while amelioration :
    # Création d'une partition
    for i in range(n):
        diste = [np.linalg.norm(X[i, :]-centres[k]) for k in range(m)]
        Y[i] = np.argmin(diste)
    # Calcul des centres de gravités
    XY = np.concatenate((Y, Y), axis=1)
    for k in range(m):
        Selection = XY[np.where(XY[:,p] == k)]
        Groupe_k = Selection[:, 0:p]
        if Groupe_k.shape[0] > 0:
            centres[k, :] = np.mean(Groupe_k, axis=0)
    # Calcul de l'inertie intra-classes
    old_I_intra = new_I_intra
    dists = [np.power(X[i, :] -centres[int(Y[i])], 2) for i in range(n)]
    new_I_intra = np.sum(dists)/n
    print("Intertie intra : ", new_I_intra)
    amelioration(old_I_intra > new_I_intra)

    print("Les centres des gravites des classes : ")
    print(centres)
    print("La partition en ", m, " Classe : ")
    print(Y.T)

# Viualisation du nuage des points
colors_individu = []
for i in range(n):
    colors_individu.append(color_classe[int(Y[i])])

fig, ax = plt.subplots()
ax.scatter(X[:, 0], X[:, 1], colors_individu)

for k in range(m):
    ax.annotate('G'+str(k+1), (centres[k, 0], centres[k, 1]), fontsize=20, c='k')

ax.set_title('Les classes convergence ')
plt.show()
