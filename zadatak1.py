import rasterio
import numpy as np
import os

# Provjerite postoji li mapa 'output_zadatak1', ako ne, stvorite je
output_dir = 'output_zadatak1'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Otvorimo TIFF datoteku koristeći rasterio
data = rasterio.open('data/response_bands.tiff')
if data is None:
    raise IOError('Nije moguće otvoriti response_bands.tiff')

# Učitavanje odgovarajućih traka iz TIFF datoteke
red_band = data.read(4)     # Crvena traka
nir_band = data.read(8)     # NIR traka (blizu infracrvena)
swir_band = data.read(11)   # SWIR traka (kratkovalna infracrvena)
cloud_mask = data.read(10)  # Maska oblaka

# Funkcija za izračun indeksa (NDVI i NDMI)
def calculate_index(a, b):
    return (a - b) / (a + b)

# Izračun NDVI (Normalizirani diferencialni vegetacijski indeks)
with np.errstate(divide='ignore', invalid='ignore'):
    ndvi = calculate_index(nir_band, red_band)
    ndvi[ndvi == np.inf] = np.nan  # Zamjena beskonačnih vrijednosti s NaN
    ndvi[cloud_mask == 1] = np.nan  # Postavljanje NaN za područja s oblakom
    ndvi = np.nan_to_num(ndvi, nan=-999)  # Zamjena NaN s NoData vrijednošću

# Izračun NDMI (Normalizirani diferencialni indeks vodenih resursa)
with np.errstate(divide='ignore', invalid='ignore'):
    ndmi = calculate_index(nir_band, swir_band)
    ndmi[ndmi == np.inf] = np.nan  # Zamjena beskonačnih vrijednosti s NaN
    ndmi[cloud_mask == 1] = np.nan  # Postavljanje NaN za područja s oblakom
    ndmi = np.nan_to_num(ndmi, nan=-999)  # Zamjena NaN s NoData vrijednošću

# Funkcija za spremanje NumPy array kao GeoTIFF
def save_tiff(data, filename, source_raster):
    profile = source_raster.profile
    profile.update(
        dtype=rasterio.float32,
        count=1,  # Jedan kanal
        nodata=-999  # NoData vrijednost
    )

    with rasterio.open(filename, 'w', **profile) as dst:
        dst.write(data, 1)

# Spremanje NDVI i NDMI kao GeoTIFF
save_tiff(ndvi, 'output_zadatak1/ndvi.tiff', data)
save_tiff(ndmi, 'output_zadatak1/ndmi.tiff', data)

# Funkcija za izračun prosječne vrijednosti, izostavljajući NoData vrijednosti
def calculate_avg(data):
    return np.mean(data[data > -999])

# Izračun prosječnih vrijednosti NDVI i NDMI
ndvi_avg = calculate_avg(ndvi)
ndmi_avg = calculate_avg(ndmi)

# Ispis prosječnih vrijednosti
print(f'Prosječni NDVI: {ndvi_avg}')
print(f'Prosječni NDMI: {ndmi_avg}')

# Ispis broja kanala u satelitskoj snimci
band_num = data.count
print(f'Satelitska snimka sadrži {band_num} kanala.')
