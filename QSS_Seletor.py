# QSS on PyQt with Seletor


from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

#  Grid Layout Design Program
class MainWindow(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Applicationssss")
       
        self.setFixedSize(QSize(400 , 250))

        # Vertival Box layout
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.setLayout(vbox)

        # widget
        mesaage = QLabel("Chanison")
        mesaage.setObjectName("danger")
        btn1 = QPushButton("Open")
        btn2 = QPushButton("Save")
        btn3 = QPushButton("Exit")
        btn3.setObjectName("danger")

        # Add Widget to layiout
        vbox.addWidget(mesaage)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)








        
# Run Program
app = QCoreApplication.instance()
if app is None :
    app = QApplication([])
    with open('style.qss' , 'r') as style :
        app.setStyleSheet(style.read())

window = MainWindow()
window.show()
app.exec()