import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700,250,500,500) # (x,y,width,height)
        self.setWindowIcon(QIcon("Monkey.png"))
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.checkbox.setChecked(False) # if "True" it will load with it already checked
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self,state):
        # print(state)
        # if state == 2: # "2" is checked and "0" is unchecked but this code is hard to read especially for others
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You do not like food")
         

def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()