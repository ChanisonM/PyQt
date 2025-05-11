from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication , QWidget , QLabel , QPushButton

#  Design Program
class MainWindow(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Applicationssss")
        lb = QLabel("Hello Python" , self)
        lb.move(150,0)
        btn = QPushButton("Click Me !!" , self)
        btn.move(150,50)


# Run Program
app = QCoreApplication.instance()
if app is None :
    app = QApplication([])

window = MainWindow()
window.show()
app.exec()