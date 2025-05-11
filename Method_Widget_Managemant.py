# Method Widget Managemant


from PyQt6.QtCore import QCoreApplication , QSize
from PyQt6.QtWidgets import QApplication , QWidget , QPushButton  , QHBoxLayout

#  Grid Layout Design Program
class MainWindow(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Applicationssss")
       
        self.setFixedSize(QSize(400 , 300))

     
        hbox = QHBoxLayout()
        self.setLayout(hbox)
        message = ["Open" , "Save" , "Exit"]
        for i in message :
            self.display_button(i , hbox)


    def display_button(self , text , layout):
        btn = QPushButton(text)
        btn.setFixedSize(QSize(100,50))
        layout.addWidget(btn)


        
# Run Program
app = QCoreApplication.instance()
if app is None :
    app = QApplication([])

window = MainWindow()
window.show()
app.exec()