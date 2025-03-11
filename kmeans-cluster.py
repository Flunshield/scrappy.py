import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Charge les données depuis le fichier CSV
df = pd.read_csv('iris_flower_data.csv')

# Affiche les noms des colonnes pour vérifier
print("Noms des colonnes : ", df.columns)

# Vérifie le début des données pour voir les colonnes
print(df.head())

# Ajuste les colonnes en fonction du CSV généré
X = df[['Sepal length', 'Sepal width', 'Petal length', 'Petal width']]

# Normalise les données pour de meilleures performances du modèle K-Means
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Applique K-Means avec 3 clusters (nous savons que le dataset Iris a 3 espèces)
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Ajoute les noms des familles (espèces) en fonction des clusters
# Nous savons que le dataset Iris a trois classes: setosa, versicolor et virginica
# Cré un mappage des clusters aux espèces
species_mapping = {
    0: 'I. setosa',
    1: 'I. versicolor',
    2: 'I. virginica'
}

# Applique le mappage pour renommer les clusters par les espèces
df['Cluster_Name'] = df['Cluster'].map(species_mapping)

# Affiche les centres des clusters
print(f"Centres des clusters :\n{kmeans.cluster_centers_}")

# Visualise les clusters sur un graphique en 2D (utilisation de PCA pour la réduction de dimensions)
from sklearn.decomposition import PCA

# Réduit les données à 2 dimensions pour la visualisation
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Ajoute les résultats de la PCA au DataFrame
df['PCA1'] = X_pca[:, 0]
df['PCA2'] = X_pca[:, 1]

# Crée un graphique de dispersion pour visualiser les clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster_Name', data=df, palette='Set1', s=100, marker='o')

# Ajoute les centres des clusters à la visualisation
centers_pca = pca.transform(kmeans.cluster_centers_)
plt.scatter(centers_pca[:, 0], centers_pca[:, 1], c='red', s=200, marker='X', label='Centres des clusters')

# Affiche les labels et le titre
plt.title('Visualisation des clusters K-Means sur le Dataset Iris')
plt.xlabel('Composante principale 1')
plt.ylabel('Composante principale 2')
plt.legend(title='Espèce')
plt.show()
