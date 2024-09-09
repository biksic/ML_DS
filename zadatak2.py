import requests
import geopandas as gpd
from io import StringIO
import os

# Provjerite postoji li mapa 'output_zadatak2', ako ne, stvorite je
output_dir = 'output_zadatak2'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# URL s kojeg dohvaćamo podatke
url = 'https://plovput.li-st.net/getObjekti/'

# Pošaljite GET zahtjev na API
response = requests.get(url)

# Provjerite je li zahtjev bio uspješan
if response.status_code == 200:
    # Učitavanje podataka u GeoDataFrame iz stringa
    gdf = gpd.read_file(StringIO(response.text))
else:
    print(f'Greška pri dohvatanju podataka s API-ja: {response.status_code}')
    raise SystemExit('Prestanak rada zbog greške pri dohvatanju podataka.')

# Ispis broja objekata sigurnosne plovidbe
num_objects = len(gdf)
print(f'Broj objekata sigurnosne plovidbe: {num_objects}')

# Filtriranje objekata sa specifičnim tipom objekta
gdf16 = gdf[gdf['tip_objekta'] == 16]

# Ispis broja objekata sa tipom objekta 16
num_objects16 = len(gdf16)
print(f'Broj objekata sigurnosne plovidbe s tipom objekta 16: {num_objects16}')

# Spremite filtrirane podatke u GeoJSON format
gdf16.to_file(os.path.join(output_dir, 'tip_objekta_16.geojson'), driver='GeoJSON')
