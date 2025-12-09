import sys
from PySide6 import QtCore,QtWidgets,QtGui
from PySide6.QtGui import QPixmap, QAction
from PySide6.QtCore import Qt,QSize
import threading

app=QtWidgets.QApplication([])

class Subs(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.layout=QtWidgets.QGridLayout(self)
        self.subtext=QtWidgets.QLabel("")
        self.subtext.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.subtext,0,0)

widgetdva=Subs()
widgetdva.setMaximumSize(100,35)
widgetdva.setMinimumSize(100,35)

class マナ(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.pixmap=QPixmap('Andrei_tarkovsky_stamp_russia_2007.jpg')
        self.label=QtWidgets.QLabel(self)
        self.label.setPixmap(self.pixmap)
        
        self.myQMenuBar = QtWidgets.QMenuBar(self)
        exitMenu = self.myQMenuBar.addMenu('Actions')
        exitAction = QtGui.QAction('Ping', self)        
        exitAction.triggered.connect(self.showsubs)
        exitMenu.addAction(exitAction)

    def showsubs(self):
        if widgetdva.isVisible() == True:
            widgetdva.hide()
        else:
            widgetdva.show()
            widgetdva.subtext.setText("Hallo Deutschland!")
            timer=threading.Timer(5,widgetdva.hide)
            timer.start()


widget=マナ()
widget.setMaximumSize(200,281)
widget.setMinimumSize(200,281)
widget.show()
sys.exit(app.exec())