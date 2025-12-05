import sys
from PySide6 import QtCore,QtWidgets,QtGui

class マナ(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        
        self.layout=QtWidgets.QGridLayout(self)
        self.box=QtWidgets.QPushButton("マナ")
        self.box.setMinimumSize(150,200)
        self.layout.addWidget(self.box)
        
app=QtWidgets.QApplication([])
widget=マナ()
widget.resize(100,100)
widget.show()
sys.exit(app.exec())