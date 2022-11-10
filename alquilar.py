from PySide6.QtWidgets import (QMainWindow,QLabel, QVBoxLayout,QWidget, QPushButton,QLineEdit)

class ventanaAlquilar(QMainWindow):
    def __init__(self, listaStock,stock):
        super().__init__()
        self.listaStock=listaStock
        self.stock= stock
        self.layout = layout = QVBoxLayout()
        self.setWindowTitle("Alquilar")
        self.texto = QLabel('Título de película a alquilar: ')
        layout.addWidget(self.texto)

        self.title = QLineEdit()
        layout.addWidget(self.title)     

        self.boton = QPushButton('alquilar')
        self.boton.setDefault(True) 
        layout.addWidget(self.boton) 
        self.boton.clicked.connect(self.alquilar)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget) 
    def alquilar(self):
        for peli in self.listaStock:
            titulo = peli.getTitulo().upper()
            inputTitulo = self.title.text().upper()
            if peli.getEstado() == 'NO alquilada' and titulo.startswith(inputTitulo) and len(inputTitulo)>=7:
                self.stock.alquilarPelicula(peli.getTitulo())
                mensaje = QLabel(f'{peli.getTitulo()} fue alquilada.')
                self.layout.addWidget(mensaje)
            elif peli.getEstado() == 'NO alquilada' and len(inputTitulo)<=6 and titulo == inputTitulo:
                self.stock.alquilarPelicula(peli.getTitulo())
                mensaje = QLabel(f'{peli.getTitulo()} fue alquilada.')
                self.layout.addWidget(mensaje)
