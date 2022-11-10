from PySide6.QtWidgets import (QMainWindow,QLabel, QVBoxLayout,QWidget, QPushButton, QLineEdit)

class ventanaFichaP(QMainWindow):
    def __init__(self, listaStock):
        super().__init__()
        self.listaStock=listaStock
        self.layout = layout = QVBoxLayout()
        self.setWindowTitle("Ficha")
        self.texto = QLabel('título de película a buscar: ')
        layout.addWidget(self.texto)

        self.title = QLineEdit()
        layout.addWidget(self.title)
        
        self.boton = QPushButton('Conseguir Ficha') 
        self.boton.setDefault(True) 
        layout.addWidget(self.boton) 
        self.boton.clicked.connect(self.getFicha)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        
    def getFicha(self):
        for peli in self.listaStock:
            titulo = peli.getTitulo().upper()
            inputTitulo = self.title.text().upper()
            self.ficha = QLabel(f'''
                        FICHA DE LA PELICULA    
                        Título: {peli.getTitulo()}
                        Género: {peli.getGenero()}
                        Año: {peli.getYear()}
                        Director: {peli.getDirector()}
                        Protagonista: {peli.getProtagonista()}
                        Precio: {peli.getPrecio()}
                        Estado: {peli.getEstado()}''')
            if len(inputTitulo)<=6 and titulo==inputTitulo:
                self.layout.addWidget(self.ficha)
                self.boton.close()
                self.title.close()
                self.texto.close()
            elif titulo.startswith(inputTitulo) and len(inputTitulo)>=7:
                self.layout.addWidget(self.ficha)
                self.boton.close()
                self.title.close()
                self.texto.close()
                
                


