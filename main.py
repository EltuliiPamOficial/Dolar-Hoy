from PyQt5 import QtWidgets, uic
from bs4 import BeautifulSoup
import requests

### Web Scraping ###

#Extracting the data from the website
url = 'https://dolarhoy.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Blue Dollar Price

#Purchase Price

db_compra = soup.find_all('div', class_='compra')

dolar_blue_compra = db_compra[0].text

#Sales Price

db_venta = soup.find_all('div', class_='venta')

dolar_blue_venta = db_venta[0].text

### Web Scraping. ###

# Iniciar La Aplicacion
app = QtWidgets.QApplication([])

# Cargar Archivos .Ui
interfaz = uic.loadUi('Assets/Interfaz.ui')

# Hacer Funcionar Los Objetos. 
def Salir():
    app.exit()

interfaz.label_2.setText(f"{dolar_blue_compra}")
interfaz.label_3.setText(f"{dolar_blue_venta}")

interfaz.pushButton.clicked.connect(Salir)

# Ejecutable
interfaz.show()
app.exec()