import sys
from PySide6 import QtCore,QtWidgets,QtGui
from PySide6.QtGui import QPixmap

class マナ(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.pixmap=QPixmap('Andrei_tarkovsky_stamp_russia_2007.jpg')
        self.label=QtWidgets.QLabel(self)
        self.label.setPixmap(self.pixmap)
        
app=QtWidgets.QApplication([])
widget=マナ()
widget.setMaximumSize(200,281)
widget.setMinimumSize(200,281)
widget.show()
sys.exit(app.exec())