from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
import subprocess


class MainWindow(QMainWindow):
    def __init__(self, loader):
        super().__init__()

        # Load the UI file
        self.ui = loader.load("gui_v1.ui", self)

        self.ui.show()

##################################################################################
#         # connect ui that will change or needs user input to their corresponding methods - eg. self.ui.runButton.clicked.connect(self.run_autoeditor)
# print(uniform_check)
        # self.ui.silentInput1.valueChanged.connect(lambda value: print("hi"))

        self.ui.silentInput1.valueChanged.connect(self.sinput1Change)
        self.ui.silentInput2.valueChanged.connect(self.sinput2Change)

        self.ui.motionlessSliderInput.valueChanged.connect(self.sliderChange)
        self.ui.motionlessPercentInput.valueChanged.connect(self.minputChange)

        self.ui.clearButton.clicked.connect(self.resetInput)

        self.ui.exportButton.clicked.connect(self.run_autoeditor)

##################################################################################

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
        self.ui.editOrderInput.setCurrentIndex(0)
        self.ui.exportProgramInput.setCurrentIndex(0)

    def run_autoeditor(self):
        # if i want to run just audio, its "auto-editor test5.mp4 --edit audio:-25dB"
        # if i want to run just motion, its "auto-editor test5.mp4 --edit motion:threshold=0.02"
        # if i want to run both, its 'auto-editor test5.mp4 --edit "(or audio:-25dB motion:0.50)" '.
        # Problem is, it will delete audio below -25db but keep the motion if its above 0.50, regardless of audio / keeps audio regardless of motion. I need to do one command after the other if I want to make sure all parts with audio below -25db is deleted and then all parts w/motion below threshold is deleted (and vice versa). Order matters.

        audio_command = ["auto-editor",
                         "test5.mp4",
                         "--margin",
                         f"{self.ui.silentInput1.value()}s,"
                         f"{self.ui.silentInput2.value()}s",
                         "--edit", f"audio:{self.ui.audioCutInput.value()}dB",
                         "--output",
                         "output.mp4"]

        motion_command = ["auto-editor",
                          "test5.mp4",
                          "--margin",
                          f"{self.ui.silentInput1.value()}s",
                          f"{self.ui.silentInput2.value()}s",
                          "--edit", f"motion:threshold="
                          f"{self.ui.motionlessPercentInput.value()}",
                          "--output",
                          "output.mp4"]

        default_both_command = ["auto-editor",
                                "test5.mp4",
                                "--margin",
                                f"{self.ui.silentInput1.value()}s",
                                f"{self.ui.silentInput2.value()}s",
                                "--edit", f"(or audio:"
                                f"{self.ui.audioCutInput.value()}"
                                f"motion:{
                                    self.ui.motionlessPercentInput.value()}",
                                "--output",
                                "output.mp4"],

        command = []
        match self.ui.editOrderInput.currentText():
            case "audio only":
                command = audio_command.copy()
                command.extend(
                    ["--export", self.ui.exportProgramInput.currentText()])
                # subprocess.run([command])
            case "motion-only":
                command = motion_command.copy()
                command.extend(
                    ["--export", self.ui.exportProgramInput.currentText()])
            case "audio then motion":
                try:
                    subprocess.run(audio_command, check=True)
                    print("Command executed successfully!")
                except subprocess.CalledProcessError as e:
                    print(f"Error occurred: {e}")
                # subprocess.run([audio_command])
                command = motion_command.copy()
                command[1] = "output.mp4"
                command.extend(
                    ["--export", self.ui.exportProgramInput.currentText()])
            case "motion then audio":
                try:
                    subprocess.run(motion_command, check=True)
                    print("Command executed successfully!")
                except subprocess.CalledProcessError as e:
                    print(f"Error occurred: {e}")
                # subprocess.run([motion_command])
                command = audio_command.copy()
                command[1] = "output.mp4"
                command.extend(
                    ["--export", self.ui.exportProgramInput.currentText()])
            case "keep both":  # default case is doing both at the same time
                command = default_both_command.copy()
                command.extend(
                    ["--export", self.ui.exportProgramInput.currentText()])

        if (self.ui.cutOrSplitInput.currentText() == "Split"):
            command.extend(["--silent-speed", "1", "--video-speed", "1"])

        try:
            subprocess.run(command, check=True)
            print("Command executed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")
