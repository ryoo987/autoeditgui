from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtUiTools import QUiLoader
from MainWindow import MainWindow

import sys

loader = QUiLoader()
app = QApplication(sys.argv)

window = MainWindow(loader)

app.exec()
