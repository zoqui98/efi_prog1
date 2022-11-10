from PySide6.QtWidgets import (QLineEdit)
from PySide6.QtGui import QIntValidator,QDoubleValidator

class InputInt(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setValidator(QIntValidator()) 

class InputFloat(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setValidator(QDoubleValidator().setNotation(QDoubleValidator.Notation.StandardNotation))
        