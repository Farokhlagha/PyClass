from PySide6.QtWidgets import (QApplication, QLineEdit)
from PySide6.QtUiTools import QUiLoader


def sub():
    global a
    a = int(main_window.txtbox.text()) # Line Edit
    main_window.txtbox.setText('')
   

def result():
    b = int(main_window.txtbox.text())
    c = a - b
    main_window.txtbox.setText(str(c))


app =  QApplication([])

loader = QUiLoader()
main_window = loader.load('main.ui')
main_window.show()


main_window.btn_sub.clicked.connect(sub) # Push Button
main_window.btn_equal.clicked.connect(result)

app.exec()