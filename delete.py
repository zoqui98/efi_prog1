from PySide6.QtWidgets import (QMainWindow,QLabel, QVBoxLayout,QWidget, QPushButton,QLineEdit)

class ventanaDelete(QMainWindow):
    def __init__(self, listaStock,stock):
        super().__init__()
        self.listaStock=listaStock
        self.stock= stock
        self.layout = layout = QVBoxLayout()
        self.setWindowTitle("Eliminar")
        
        self.texto = QLabel('Título de película a eliminar: ')
        layout.addWidget(self.texto)

        self.title = QLineEdit()
        layout.addWidget(self.title)

        self.boton = QPushButton('eliminar')
        self.boton.setDefault(True) 
        layout.addWidget(self.boton) 
        self.boton.clicked.connect(self.eliminar)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget) 

    def eliminar(self):
        for peli in self.listaStock:
            titulo = peli.getTitulo().upper()
            inputTitulo = self.title.text().upper()
            if inputTitulo == titulo:
                mensaje = QLabel(f'La pelicula "{peli.getTitulo()}" fue eliminada.')
                self.layout.addWidget(mensaje)
                self.stock.deletePelicula(peli.getTitulo())

