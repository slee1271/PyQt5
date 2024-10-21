import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon #for icon on the top left corner
from PyQt5.QtGui import QFont #for fonts of the labels
from PyQt5.QtCore import Qt #for alignments of labels

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700,250,500,500) # (x,y,width,height)
        self.setWindowIcon(QIcon("Monkey.png"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: #b700ff;"
                            "background-color: #00b7ff;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        # label.setAlignment(Qt.AlignTop) #Vertically top
        # label.setAlignment(Qt.AlignBottom) #Vertically bottom
        # label.setAlignment(Qt.AlignVCenter) #Vertically center
        # label.setAlignment(Qt.AlignRight) #Horizontally right
        # label.setAlignment(Qt.AlignLeft) #Horizontally left
        # label.setAlignment(Qt.AlignHCenter) #Horizontally center
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #Combine two alignments
        label.setAlignment(Qt.AlignCenter) #Center for both vertical and horizontal



def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()