# pip install pyside6 = Qt
# pyside6-designer

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

Akbar = 'reza'

def test():
    print('Salam Salam 🙋‍♀️')

def say_hello():
    my_window.lineEdit.setText('Hello Qt 😊')

my_app = QApplication([])

loader = QUiLoader()
my_window = loader.load('mainwindow.ui')
my_window.show()

my_window.pushButton_2.clicked.connect(test)
my_window.Akbar.clicked.connect(say_hello) # changed name pushButton to Akbar
# name inside the button change to  اکبر اقا
# with Qi design (text)
my_app.exec()


