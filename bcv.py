import requests
from datetime import date
from bs4 import BeautifulSoup

url = 'https://www.bcv.org.ve'
hoy = date.today()
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" }
respuesta = requests.get(url,headers=headers, verify=False, timeout=10)
respuesta.encoding = "utf-8"

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    tasafinder = soup.find('div', id = "dolar")
    if tasafinder:
        strong = tasafinder.find('strong', class_='strong-tb')
        cuptext = strong.get_text(strip=True)
        numberbcv = float(cuptext.replace(",", "."))
    print(f"La tasa del {hoy} es {numberbcv}")
else: 
    print("No se encontró el contenedor con id 'dolar'")
        