from PySide6.QtWidgets import (QMainWindow,QLabel, QVBoxLayout,QWidget, QPushButton,QLineEdit)

class ventanaDevolucion(QMainWindow):
    def __init__(self, listaStock,stock):
        super().__init__()
        self.listaStock=listaStock
        self.stock= stock
        self.layout = layout = QVBoxLayout()
        
        self.texto = QLabel('Título de película que se devuelve: ')
        layout.addWidget(self.texto)

        self.title = QLineEdit()
        layout.addWidget(self.title)     

        self.boton = QPushButton('Devolver')
        self.boton.setDefault(True) 
        layout.addWidget(self.boton) 
        self.boton.clicked.connect(self.devolucion)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget) 
    def devolucion(self):
        for peli in self.listaStock:
            titulo = peli.getTitulo().upper()
            inputTitulo = self.title.text().upper()
            if peli.getEstado() == 'Alquilada' and len(inputTitulo)<=6 and titulo==inputTitulo:
                self.stock.devolverPelicula(peli.getTitulo())
                mensaje = QLabel(f'{peli.getTitulo()} fue devuelta.')
                self.layout.addWidget(mensaje)
            elif peli.getEstado() == 'Alquilada' and titulo.startswith(inputTitulo) and len(inputTitulo)>=7:
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                self.stock.devolverPelicula(peli.getTitulo())
                mensaje = QLabel(f'{peli.getTitulo()} fue devuelta.')
                self.layout.addWidget(mensaje)
              
