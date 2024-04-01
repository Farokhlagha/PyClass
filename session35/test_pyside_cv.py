import sys
import cv2
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
import cv2
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.my_btn = QPushButton()
        self.my_btn.setText('Hello World!')
        layout.addWidget(self.my_btn)

        self.my_lable = QLabel()
        layout.addWidget(self.my_lable)

        image = cv2.imread('input/pepers.jpg')        # open with opencv
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # BGR to RGB
        image_qt = QImage(image, image.shape[1], image.shape[0], QImage.Format.Format_RGB888) # change to Qimage
        image_qpixmap = QPixmap.fromImage(image_qt)           # change to Qpixmap
        self.my_lable.setPixmap(image_qpixmap)                # display image in lable

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
       

if __name__== '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    app.exec()