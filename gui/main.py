from PySide6.QtWidgets import QApplication
# from PySide6.QtUiTools import QUiLoader
from MainWindow import MainWindow

import sys

# loader = QUiLoader()
app = QApplication(sys.argv)
window = MainWindow(app)
window.show()

app.exec()
