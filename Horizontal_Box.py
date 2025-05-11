from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication , QWidget , QPushButton , QHBoxLayout

#  Horizontal Box Layout Design Program
class MainWindow(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Applicationssss")


        # Create layout & Setting
        hbox = QHBoxLayout(self)
        self.setLayout(hbox)

        # Button Widget 
        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")

        # Add Widget on layout
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        
# Run Program
app = QCoreApplication.instance()
if app is None :
    app = QApplication([])

window = MainWindow()
window.show()
app.exec()