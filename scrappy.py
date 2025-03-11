import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la page Wikipedia
url = 'https://en.wikipedia.org/wiki/Iris_flower_data_set'

# Effectu une requête HTTP GET pour obtenir le contenu de la page
response = requests.get(url)

# Vérifie si la requête a réussi
if response.status_code == 200:
    print("Requête réussie, extraction des données...")
    
    # Parse le contenu de la page avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trouve le tableau contenant les données (le premier tableau sur la page)
    table = soup.find('table', {'class': 'wikitable'})
    
    # Extrait les en-têtes du tableau
    headers = [header.text.strip() for header in table.find_all('th')]
    
    # Extrait les lignes de données du tableau
    rows = []
    for row in table.find_all('tr')[1:]:  # Ignorer la première ligne (en-têtes)
        cells = row.find_all('td')
        if len(cells) > 0:
            data = [cell.text.strip() for cell in cells]
            rows.append(data)
    
    # Crée un DataFrame pandas pour structurer les données
    df = pd.DataFrame(rows, columns=headers)
    
    # Affiche les 5 premières lignes du DataFrame
    print(df.head())
    
    # Sauvegarde les données dans un fichier CSV
    df.to_csv('iris_flower_data.csv', index=False)
    print("Données sauvegardées dans 'iris_flower_data.csv'")
else:
    print(f"Erreur lors de la requête HTTP: {response.status_code}")
