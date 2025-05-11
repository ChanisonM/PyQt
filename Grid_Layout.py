from PyQt6.QtCore import QCoreApplication , QSize
from PyQt6.QtWidgets import QApplication , QWidget , QPushButton , QGridLayout

#  Grid Layout Design Program
class MainWindow(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Applicationssss")
        # self.setFixedHeight(400)
        # self.setFixedWidth(600)
        self.setFixedSize(QSize(300 , 300))


        # Create layout & Setting
        grid = QGridLayout(self)
        # self.setLayout(grid)

        # Button Widget 
        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn2.setFixedSize(QSize(50,50))
        btn3 = QPushButton("3")
        btn4 = QPushButton("4")

        # Add Widget on layout
        grid.addWidget(btn1 , 0 , 0)
        grid.addWidget(btn2 , 0 , 1)
        grid.addWidget(btn3 , 1 , 0)
        grid.addWidget(btn4 , 1 , 1)
        


        
# Run Program
app = QCoreApplication.instance()
if app is None :
    app = QApplication([])

window = MainWindow()
window.show()
app.exec()