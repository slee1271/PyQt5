import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap #for the image


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700,250,500,500) # (x,y,width,height)
        self.setWindowIcon(QIcon("Monkey.png"))

        label = QLabel(self)
        label.setGeometry(0,0,250,250)

        pixmap = QPixmap("Monkey.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        # #set picture to bottom right
        # label.setGeometry(self.width() - label.width(),
        #                    self.height() - label.height(),
        #                      label.width(), label.height())

        #set picture to the center
        label.setGeometry((self.width() - label.width()) // 2,
                           (self.height() - label.height()) // 2,
                             label.width(), label.height())



def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()