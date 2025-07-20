import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from beatleaderApi import getBLdata

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Beatleader Profile Viewer")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon(resource_path('assests/beatleaderIcon.png')))
        self.setStyleSheet("background-color: #242424;")

        # Load custom font
        QFontDatabase.addApplicationFont(resource_path("assests/BLfont.ttf"))
        self.font = QFont("BLfont", 24)

        # Make the labels
        self.displayname = QLabel(" ", self)
        self.displayrank = QLabel(" ", self)
        self.displaypp = QLabel(" ", self)
        self.displayavgrank = QLabel(" ", self)
        self.displayProfilePicture = QLabel(" ", self)

        # Set positions
        self.displayname.setGeometry(0, 100, 500, 50)
        self.displayrank.setGeometry(0, 150, 500, 50)
        self.displaypp.setGeometry(0, 200, 500, 50)
        self.displayavgrank.setGeometry(0, 250, 500, 50)

        # Style labels
        self.style(self.displayname)
        self.style(self.displayrank)
        self.style(self.displaypp)
        self.style(self.displayavgrank)

        # Icon in the window
        icon = QLabel(self)
        icon_pixmap = QPixmap(resource_path('assests/beatleaderIcon.png'))
        icon.setPixmap(icon_pixmap)
        icon.setScaledContents(True)
        icon.setGeometry((self.width() - 100) // 2, 0, 100, 100)

        # Input bar
        self.idInput = QLineEdit(self)
        self.idInput.setPlaceholderText("Enter a Beatleader ID")
        self.idInput.setGeometry(0, 350, 400, 50)
        self.idInput.setStyleSheet("font-size: 25px; background-color: white; font-family: BLfont;")

        # Submit button
        self.submit = QPushButton("Submit", self)
        self.submit.setGeometry(400, 350, 100, 50)
        self.submit.setStyleSheet("font-size: 25px; background-color: white; font-family: BLfont;")
        self.submit.setFont(self.font)

        self.submit.clicked.connect(self.sendData)

    def style(self, label):
        label.setFont(QFont("BLfont", 30))
        label.setStyleSheet("color: white; font-size: 30px;")
        label.setAlignment(Qt.AlignCenter)

    def sendData(self):
        user_id = self.idInput.text()
        self.display_profile(user_id)
        self.displaypfp(user_id)

    def display_profile(self, user_id):
        name = getBLdata.getName(user_id)
        rank = getBLdata.getRank(user_id)
        pp = getBLdata.getPP(user_id)
        avg_rank = getBLdata.getAvgRank(user_id)

        self.displayname.setText(name)
        self.displayrank.setText(rank)
        self.displaypp.setText(str(pp))
        self.displayavgrank.setText(avg_rank)

    def displaypfp(self, user_id):
        # Profile picture
        pixmap = getBLdata.getAvatarPixmap(user_id)
        #print(user_id)
        if pixmap:
            pixmap.scaled(100,100)
            self.displayProfilePicture.setPixmap(pixmap)
            self.displayProfilePicture.setGeometry(0, 100, 100, 100)
            self.displayProfilePicture.setScaledContents(True)
            self.displayProfilePicture.move(10,10)
            self.displayProfilePicture.show()
        #else:
            #print("error handeling play avatar")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
