from PySide6.QtWidgets import (QLineEdit,QPushButton,QLabel, QVBoxLayout,QWidget,)
from inputValido import *

class ventanaActualizarP(QWidget):
    def __init__(self, listaStock, stock):
            super().__init__()
            self.layout = layout = QVBoxLayout()
            self.setLayout(layout)
            self.listaStock = listaStock
            self.stock = stock
            self.setWindowTitle("Actualizar precio")
            self.mensaje = QLabel('titulo de la pelicula a actualizar precio: ')
            layout.addWidget(self.mensaje) 
            self.titulo = QLineEdit() 
            layout.addWidget(self.titulo)
            
            self.mensaje = QLabel('ingrese el nuevo precio de la pelicula: ')
            layout.addWidget(self.mensaje) 
            self.precio = QLineEdit() 
            layout.addWidget(self.precio)
            
            self.botonModificar = QPushButton(f"Modificar")
            self.botonModificar.setDefault(True) 
            layout.addWidget(self.botonModificar) 
            self.botonModificar.clicked.connect(self.actualizarPrecio)

    def actualizarPrecio(self):
        for peli in self.listaStock:
            titulo = peli.getTitulo().upper()
            inputTitulo = self.titulo.text().upper()
            if len(inputTitulo)<=6 and titulo==inputTitulo:
                mensaje = QLabel(f'Precio actualizado de {peli.getTitulo()}.')
                self.layout.addWidget(mensaje)
                self.stock.modificarPrecio(peli.getTitulo(), float(self.precio.text()))
            elif titulo.startswith(inputTitulo) and len(inputTitulo)>=7:
                mensaje = QLabel(f'Precio actualizado de {peli.getTitulo()}.')
                self.layout.addWidget(mensaje)
                self.stock.modificarPrecio(peli.getTitulo(), float(self.precio.text()))