from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,QWidget, QPushButton)
from qt_material import apply_stylesheet
from baseDeDatos import *
from stockCompleto import *
from ventanaStock import *
from anadirPeli import *
from fichaPeli import *
from actualizarPrecio import *
from alquilar import *
from pelisAlquiladas import *
from devolucion import *
from delete import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.stock = Stock()
        self.setWindowTitle("Menú Principal")        

        self.layout = layout = QVBoxLayout()

        self.botonStock = QPushButton('Ver stock completo') 
        self.botonStock.setDefault(True) 
        layout.addWidget(self.botonStock) 
        self.botonStock.clicked.connect(self.getStock) 

        self.botonPelicula = QPushButton('Añadir Pelicula') 
        self.botonPelicula.setDefault(True) 
        layout.addWidget(self.botonPelicula) 
        self.botonPelicula.clicked.connect(self.getPelicula)

        self.botonFichaP = QPushButton('Ver ficha de película') 
        self.botonFichaP.setDefault(True) 
        layout.addWidget(self.botonFichaP) 
        self.botonFichaP.clicked.connect(self.getFichaP)

        self.botonActualizarP = QPushButton('Actualizar precio') 
        self.botonActualizarP.setDefault(True) 
        layout.addWidget(self.botonActualizarP) 
        self.botonActualizarP.clicked.connect(self.actualizarPrecio)

        self.botonAlquilar = QPushButton('Alquilar una película') 
        self.botonAlquilar.setDefault(True) 
        layout.addWidget(self.botonAlquilar) 
        self.botonAlquilar.clicked.connect(self.alquilar)

        self.botonPAlquiladas = QPushButton('ver lista de peliculas alquiladas') 
        self.botonPAlquiladas.setDefault(True) 
        layout.addWidget(self.botonPAlquiladas) 
        self.botonPAlquiladas.clicked.connect(self.getAlquiladas)
        
        self.botonDevolucion = QPushButton('Devolución de película') 
        self.botonDevolucion.setDefault(True) 
        layout.addWidget(self.botonDevolucion) 
        self.botonDevolucion.clicked.connect(self.devolucion)

        self.botonEliminarP = QPushButton('Eliminar pelicula del stock') 
        self.botonEliminarP.setDefault(True) 
        layout.addWidget(self.botonEliminarP) 
        self.botonEliminarP.clicked.connect(self.eliminarP)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        
    def getStock(self): 
       self.listastock = self.stock.getStock() 
       self.w = ventanaStock(self.listastock)
       self.w.show()

    def getPelicula(self): 
        self.listastock = self.stock.getStock() 
        self.w = AñadirPelicula(self.listastock,self.stock)
        self.w.show()

    def getFichaP(self): 
        self.listastock = self.stock.getStock() 
        self.w = ventanaFichaP(self.listastock)
        self.w.show()

    def alquilar(self): 
        self.listastock = self.stock.getStock() 
        self.w = ventanaAlquilar(self.listastock,self.stock)
        self.w.show()

    def actualizarPrecio(self):
        self.listastock = self.stock.getStock()
        self.w = ventanaActualizarP(self.listastock,self.stock)
        self.w.show()

    def getAlquiladas(self):
        self.listastock = self.stock.getStock() 
        self.w = ventanaAlquiladas(self.listastock)
        self.w.show()

    def devolucion(self):
        self.listastock = self.stock.getStock() 
        self.w = ventanaDevolucion(self.listastock,self.stock)
        self.w.show()

    def eliminarP(self):
        self.listastock = self.stock.getStock()
        self.w = ventanaDelete(self.listastock,self.stock)
        self.w.show()


if __name__ == '__main__':
    app = QApplication()
    apply_stylesheet(app, theme='dark_red.xml')
    window = MainWindow()
    window.show()
    app.exec()
      