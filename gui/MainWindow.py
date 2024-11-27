from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
import subprocess


class MainWindow(QMainWindow):
    def __init__(self, loader):
        super().__init__()

        # Load the UI file
        self.ui = loader.load("gui_v1.ui", self)

        self.ui.show()

##########################################################
#         # connect ui that will change or needs user input to their corresponding methods - eg. self.ui.runButton.clicked.connect(self.run_autoeditor)
# print(uniform_check)
        # self.ui.silentInput1.valueChanged.connect(lambda value: print("hi"))

        # initalize variables
        # self.initialize_var()
        # self.silentInput1 = 0.0
        # self.silentInput2 = 0.0
        # # self.uniformCheck = True
        # self.cutOrSplitChoice = "Cut Out"
        # self.motionlessSliderInput = 0
        # self.motionlessPercentInput = 0
        # self.audioCutInput = 0


# connect spinbox 1 and 2 and uniform check box
        self.ui.silentInput1.valueChanged.connect(self.sinput1Change)
        self.ui.silentInput2.valueChanged.connect(self.sinput2Change)
        # self.ui.uniformCheck.checkStateChanged.connect()

# connect choosing cut out vs split
        # self.ui.cutOrSplitInput.activated.connect()
        # i can change this variable when i export

# connect motionless scale and the spinbox
        self.ui.motionlessSliderInput.valueChanged.connect(self.sliderChange)
        self.ui.motionlessPercentInput.valueChanged.connect(self.minputChange)
# connect audio below spinbox
        # self.ui.audioCutInput.valueChanged.connect()

# connect the clear button
        self.ui.clearButton.clicked.connect(self.resetInput)

# connect the export button
        self.ui.exportButton.clicked.connect(self.run_autoeditor)

###########################################################

# # methods corresponding to ui such as
#     def run_autoeditor(self):
#         # Example CLI command
#         command = ["auto-editor", "input.mp4", "--export", "output.mp4"]

#         try:
#             subprocess.run(command, check=True)
#             print("Command executed successfully!")
#         except subprocess.CalledProcessError as e:
#             print(f"Error occurred: {e}")

# spinbox 1 and 2 will change by a tenth. They are the same number when uniform is checked. They arent the same when unchecked.
    def sinput1Change(self):
        if self.ui.uniform_checkbox.isChecked():
            self.ui.silentInput2.setValue(self.ui.silentInput1.value())

    def sinput2Change(self):
        if self.ui.uniform_checkbox.isChecked():
            self.ui.silentInput1.setValue(self.ui.silentInput2.value())


# set the variable for cut out vs split

# the motionless scale will go from 0 to 100% and needs to connect to the spinbox to reflect the slider changing. the spinbox itself needs to show % after every change


    def sliderChange(self):
        self.ui.motionlessPercentInput.setValue(
            self.ui.motionlessSliderInput.value())

    def minputChange(self):
        self.ui.motionlessSliderInput.setValue(
            self.ui.motionlessPercentInput.value())
# the audio below spinbox will change by 1 and needs a unit db after every change.

    def resetInput(self):
        self.ui.silentInput1.setValue(0.0)
        self.ui.silentInput2.setValue(0.0)
        self.ui.cutOrSplitInput.setCurrentIndex(0)
        self.ui.motionlessSliderInput.setValue(0)
        self.ui.motionlessPercentInput.setValue(0)
        self.ui.audioCutInput.setValue(0)
        # self.initialize_var()

    def run_autoeditor(self):
        command = ["auto-editor",
                   "test.mp4",
                   "--margin",
                   f"{self.ui.silentInput1.value()}s",
                   f"{self.ui.silentInput2.value()}s",
                   "--edit", f"motion:threshold={
                       self.ui.motionlessPercentInput.value()}",
                   "--edit", f"audio:threshold={
                       self.ui.audioCutInput.value()}dB",
                   "--export",
                   "output.mp4"]

        try:
            subprocess.run(command, check=True)
            print("Command executed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")

    # def initialize_var(self):
    #     self.silentInput1 = self.ui.silentInput1.value()
    #     self.silentInput2 = self.ui.silentInput2.value()
    #     # self.uniformCheck = True
    #     self.cutOrSplitChoice = self.ui.cutOrSplitInput.currentText()
    #     self.motionlessSliderInput = self.ui.motionlessSliderInput.value()
    #     self.motionlessPercentInput = self.ui.motionlessPercentInput.value()
    #     self.audioCutInput = self.ui.audioCutInput.value()
