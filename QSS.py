# QSS on PyQt


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
        hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # padding css
        hbox.setSpacing(40)
        self.setLayout(hbox)


        message = ["Open" , "Save" , "Exit"]
        for i in message :
            self.display_button(i , hbox)


    def display_button(self , text , layout):
        btn = QPushButton(text)
        btn.setFixedSize(QSize(100,50))
        # QSS or CSS
        btn.setStyleSheet(
            '''
            color : white ;
            background-color : blue ; 
            font-size : 20px ;
            font-weight : bold ;

            '''
        )
        layout.addWidget(btn)


        
# Run Program
app = QCoreApplication.instance()
if app is None :
    app = QApplication([])

window = MainWindow()
window.show()
app.exec()