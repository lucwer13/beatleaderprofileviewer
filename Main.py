import sys
import os
import time
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from beatleaderApi import getBLdata

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Beatleader Profile viewer")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon('BeatleaderIcon.png'))
        self.setStyleSheet("background-color: #242424;")

        # Making the labels
        self.displayname = QLabel(" ", self)
        self.displayrank = QLabel(" ", self)
        self.displaypp = QLabel(" ", self)
        self.displayavgrank = QLabel(" ", self)

        #Positions of the labels
        self.displayname.setGeometry(0,100,500,50)
        self.displayrank.setGeometry(0,150,500,50)
        self.displaypp.setGeometry(0,200,500,50)
        self.displayavgrank.setGeometry(0,250,500,50)

        # Styling the labels
        self.style(self.displayname)
        self.style(self.displayrank)
        self.style(self.displaypp)
        self.style(self.displayavgrank)

        # Icon in the top of the window
        iconpath = QPixmap('BeatleaderIcon.png')
        icon = QLabel(self)
        icon.setPixmap(iconpath)
        icon.setScaledContents(True)
        icon.setGeometry(0, 0, 100, 100)
        icon.setGeometry((self.width() - icon.width()) // 2, 0, icon.height(), icon.width())

        # Makes and styles the input bar
        self.idInput = QLineEdit(self)
        self.idInput.setPlaceholderText("Enter a Beatleader ID")
        self.idInput.setGeometry(0,350,400,50)
        self.idInput.setStyleSheet("font-size: 25px; background-color: white;")

        # Makes and styles the submit button
        self.submit = QPushButton("Submit", self)
        self.submit.setGeometry(400,350,100,50)
        self.submit.setStyleSheet("font-size: 25px; background-color: white;")

        # Input of the ID and sending it to the display_profile function
        self.submit.clicked.connect(self.sendData)

    def sendData(self):
        print("Button Clicked!")
        id = self.idInput.text()
        print(id)
        self.display_profile(id)


    # Styles the labels
    def style(self, theName):
        try:
            theName.setFont(QFont("Arial", 30))
            theName.setStyleSheet("color: white; font-size: 30px;")
            theName.setAlignment(Qt.AlignCenter)
        except:
            print("error styling")

    # Sets the API data on the screen
    def display_profile(self, id):
        name = getBLdata.getName(id)
        rank = getBLdata.getRank(id)
        pp = getBLdata.getPP(id)
        rankedacc = getBLdata.getAvgRank(id)

        self.displayname.setText(name)
        self.displayrank.setText(rank)
        self.displaypp.setText(str(pp))
        self.displayavgrank.setText(rankedacc)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()