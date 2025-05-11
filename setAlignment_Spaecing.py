# setAlignment and Spaecing


from PyQt6.QtCore import QCoreApplication , QSize ,Qt
from PyQt6.QtWidgets import QApplication , QWidget , QPushButton  , QHBoxLayout , QVBoxLayout 

#  Grid Layout Design Program
class MainWindow(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Applicationssss")
       
        self.setFixedSize(QSize(800 , 600))

        # Horizontal layout
        hbox = QHBoxLayout()
        # margin css
        hbox.setAlignment(Qt.AlignmentFlag.AlignRight)
        # padding css
        hbox.setSpacing(40)
        self.setLayout(hbox)


        # Vertical layout
        # vbox = QVBoxLayout()
        # vbox.setAlignment(Qt.AlignmentFlag.AlignBottom)
        # self.setLayout(vbox)

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