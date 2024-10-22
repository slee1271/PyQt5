import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700,250,500,500) # (x,y,width,height)
        self.setWindowIcon(QIcon("Monkey.png"))       
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Hello", self)
        self.initUI() 

    def initUI(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size: 30px;")

    def on_click(self):
        # print("button clicked")
        # self.button.setText("Clicked")
        # self.button.setDisabled(True)

        self.label.setText("Goodbye")

def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()