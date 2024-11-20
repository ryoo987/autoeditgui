from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
import subprocess


class MainWindow(QMainWindow):
    def __init__(self, loader):
        super().__init__()

        # Load the UI file
        self.ui = loader.load("gui_v1.ui", self)

        self.ui.show()

#         # connect ui that will change or needs user input to their corresponding methods

        self.ui.runButton.clicked.connect(self.run_autoeditor)


# # methods corresponding to ui
#     def run_autoeditor(self):
#         # Example CLI command
#         command = ["auto-editor", "input.mp4", "--export", "output.mp4"]

#         try:
#             subprocess.run(command, check=True)
#             print("Command executed successfully!")
#         except subprocess.CalledProcessError as e:
#             print(f"Error occurred: {e}")
