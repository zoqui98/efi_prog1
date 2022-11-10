from PySide6.QtWidgets import (QMainWindow,QLabel, QVBoxLayout,QWidget, QScrollArea)
from PySide6.QtCore import Qt

class ventanaAlquiladas(QMainWindow):
    def __init__(self, listaStock):
        super().__init__()
        self.scroll = QScrollArea()
        self.widget = QWidget() 
        self.layout = layout = QVBoxLayout()
        self.mensaje = QLabel('Películas alquiladas:')
        layout.addWidget(self.mensaje) 
        self.setWindowTitle("Stock alquiladas")
 
        for i in range(len(listaStock)):
              if listaStock[i].getEstado()== "Alquilada":
                self.peli = QLabel(f'Cod: {i+1}° - {listaStock[i].getTitulo()}')
                layout.addWidget(self.peli) 
        self.widget.setLayout(self.layout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.show()        