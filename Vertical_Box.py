from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication , QWidget , QPushButton , QVBoxLayout

#  Vertical Box Layout Design Program
class MainWindow(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Applicationssss")


        # Create layout & Setting
        vbox = QVBoxLayout(self)
        self.setLayout(vbox)

        # Button Widget 
        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")

        # Add Widget on layout
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        
# Run Program
app = QCoreApplication.instance()
if app is None :
    app = QApplication([])

window = MainWindow()
window.show()
app.exec()