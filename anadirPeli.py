from PySide6.QtWidgets import (QLineEdit,QPushButton,QLabel, QVBoxLayout,QWidget,)
from inputValido import *

class AñadirPelicula(QWidget):
    def __init__(self, listaStock,stock):
            super().__init__()
            layout = QVBoxLayout()
            self.setLayout(layout)

            self.stock= stock

            self.listaStock = listaStock
            ultimaPeli = self.listaStock[len(self.listaStock)-1]
            idUltima = int(ultimaPeli.getId())
            self.id = idUltima+1
            self.setWindowTitle("Añadir Película")

            self.mensaje = QLabel('ingrese el titulo de la pelicula: ')
            layout.addWidget(self.mensaje) 
            self.titulo = QLineEdit() 
            layout.addWidget(self.titulo)

            self.mensaje = QLabel('ingrese el genero de la pelicula: ')
            layout.addWidget(self.mensaje)
            self.genero = QLineEdit() 
            layout.addWidget(self.genero)
            
            self.mensaje = QLabel('ingrese el año de la pelicula: ')
            layout.addWidget(self.mensaje) 
            self.year = QLineEdit() 
            self.year = InputInt()
            layout.addWidget(self.year)
            
            self.mensaje = QLabel('ingrese los protagonistas: ')
            layout.addWidget(self.mensaje) 
            self.protagonista = QLineEdit() 
            layout.addWidget(self.protagonista)
            
            self.mensaje = QLabel('ingrese el director de la pelicula: ')
            layout.addWidget(self.mensaje) 
            self.director = QLineEdit() 
            layout.addWidget(self.director)
            
            self.mensaje = QLabel('ingrese el precio de la pelicula: ')
            layout.addWidget(self.mensaje) 
            self.precio = QLineEdit()
            self.precio = InputFloat()
            layout.addWidget(self.precio)
            
            self.botonAñadir = QPushButton(f"Agregar")
            self.botonAñadir.setDefault(True) 
            layout.addWidget(self.botonAñadir) 
            self.botonAñadir.clicked.connect(self.agregarPeli)

    def agregarPeli(self):
        self.stock.addPelicula(self.id,self.titulo.text(), self.genero.text(), self.protagonista.text(), self.director.text(), int(self.year.text()), float(self.precio.text()))
    