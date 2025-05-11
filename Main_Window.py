from PyQt6.QtCore import QCoreApplication 
from PyQt6.QtWidgets import QApplication , QWidget 
from PyQt6 import QtGui

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

app = QCoreApplication.instance()
if app is None :
    app = QApplication([])
    # icon program
    app.setWindowIcon(QtGui.QIcon('asset/icon/icon.png'))

window = MainWindow()
window.show()
app.exec()