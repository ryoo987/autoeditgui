from PySide6.QtWidgets import QMainWindow, QFileDialog
from ui_mainwindow import Ui_MainWindow
import subprocess
import re
from tqdm import tqdm
from ffmpeg_progress_yield import FfmpegProgress


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, loader):
        super().__init__()

        # Load the UI file
        # self.ui = loader.load("gui_v1.ui", self)
        self.setupUi(self)

        # self.show()

        # connect ui ##########################
        # first if the user drag drops or imports their file, do ffmpeg analysis
        self.filePath = None
        self.fileInputBtn.clicked.connect(self.importFile)

        # now account for input interactions made
        self.silentInput1.valueChanged.connect(self.sinput1Change)
        self.silentInput2.valueChanged.connect(self.sinput2Change)

        self.motionlessSliderInput.valueChanged.connect(self.sliderChange)
        self.motionlessPercentInput.valueChanged.connect(self.minputChange)

        self.audioCutSliderInput.valueChanged.connect(
            self.audioCutSliderChange)
        self.audioCutInput.valueChanged.connect(self.audioCutInputChange)

        self.clearButton.clicked.connect(self.resetInput)

        self.exportPath = None
        self.exportButton.clicked.connect(self.run_autoeditor)

##################################################################################
    # all the methods

    def importFile(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self, "Select Video File", "", "Video Files (*.mp4 *.avi *.mov);;All Files (*)")
        if filePath:
            self.filePath = filePath

        self.progressLabel.setText("Retrieving audio stats")
        audio_stats_command = ["ffmpeg",
                               "-hide_banner",
                               "-i",
                               f"{self.filePath}",
                               "-filter:a",
                               "volumedetect",
                               "-f", "null",
                               "NUL"]

        result = FfmpegProgress(audio_stats_command)
        with tqdm(total=100, position=1, desc="Test") as pbar:
            for progress in result.run_command_with_progress():
                pbar.update(progress - pbar.n)
                # print(progress)
                self.progressBar.setValue(progress)

        self.progressLabel.setText("Audio stats retrieved")

        output = result.stderr
        mean_volume = re.search(r"mean_volume:\s(-?\d+\.\d+)", output)
        mean_volume = float(mean_volume.group(1))
        max_volume = re.search(r"max_volume:\s(-?\d+\.\d+)", output)
        max_volume = float(max_volume.group(1))

        self.meanDBValue.setNum(mean_volume)
        self.maxDBValue.setNum(max_volume)


# spinbox 1 and 2 will change by a tenth. They are the same number when uniform is checked. They arent the same when unchecked.


    def sinput1Change(self):
        if self.uniform_checkbox.isChecked():
            self.silentInput2.setValue(self.silentInput1.value())

    def sinput2Change(self):
        if self.uniform_checkbox.isChecked():
            self.silentInput1.setValue(self.silentInput2.value())

# the motionless scale will go from 0 to 100% and needs to connect to the spinbox to reflect the slider changing. the spinbox itself needs to show % after every change

    def sliderChange(self):
        self.motionlessPercentInput.setValue(
            self.motionlessSliderInput.value())

    def minputChange(self):
        self.motionlessSliderInput.setValue(
            self.motionlessPercentInput.value())

# same thing for audioCut inputs
    def audioCutSliderChange(self):
        self.audioCutInput.setValue(
            self.audioCutSliderInput.value())

    def audioCutInputChange(self):
        self.audioCutSliderInput.setValue(
            self.audioCutInput.value())

# Clear button

    def resetInput(self):
        self.silentInput1.setValue(0.0)
        self.silentInput2.setValue(0.0)
        self.cutOrSplitInput.setCurrentIndex(0)
        self.motionlessSliderInput.setValue(0)
        self.motionlessPercentInput.setValue(0)
        self.audioCutInput.setValue(0)
        self.editOrderInput.setCurrentIndex(0)
        self.exportProgramInput.setCurrentIndex(0)

# Export
    def run_autoeditor(self):
        # if i want to run just audio, its "auto-editor test5.mp4 --edit audio:-25dB"
        # if i want to run just motion, its "auto-editor test5.mp4 --edit motion:threshold=0.02"
        # if i want to run both, its 'auto-editor test5.mp4 --edit "(or audio:-25dB motion:0.50)" '.
        # Problem is, it will delete audio below -25db but keep the motion if its above 0.50, regardless of audio / keeps audio regardless of motion. I need to do one command after the other if I want to make sure all parts with audio below -25db is deleted and then all parts w/motion below threshold is deleted (and vice versa). Order matters.
        self.exportPath = None
        exportPath = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "output.mp4",
            "Video Files (*.mp4 *.mkv *.mov *.avi *.webm);;All Files (*)"
        )
        if exportPath:
            self.exportPath = exportPath[0]

        audio_command = ["auto-editor",
                         f"{self.filePath}",
                         "--edit",
                         f"audio:{self.audioCutInput.value()}dB",
                         "--output",
                         "output.mp4",
                         "--progress",
                         "modern"]

        motion_command = ["auto-editor",
                          f"{self.filePath}",
                          "--edit",
                          f"motion:threshold="
                          f"{self.motionlessPercentInput.value()}",
                          "--output",
                          "output.mp4",
                          "--progress",
                          "modern"]

        default_both_command = ["auto-editor",
                                f"{self.filePath}",
                                "--edit",
                                f"(or audio:",
                                f"{self.audioCutInput.value()}",
                                f"motion:{
                                    self.motionlessPercentInput.value()}",
                                "--output",
                                f"{self.exportPath}",
                                "--progress",
                                "modern"],

        currCommandNum = 1
        command = []
        match self.editOrderInput.currentText():
            case "audio only":
                command = audio_command.copy()
                command[5] = f"{self.exportPath}"
                command.extend(
                    ["--export", self.exportProgramInput.currentText()])
            case "motion-only":
                command = motion_command.copy()
                command[5] = f"{self.exportPath}"
                command.extend(
                    ["--export", self.exportProgramInput.currentText()])
            case "audio then motion":
                self.progressLabel.setText("Process 1 of 2")
                self.runAutoWProgressBar(audio_command)

                command = motion_command.copy()
                command[1] = "output.mp4"  # change input
                command[5] = f"{self.exportPath}"
                command.extend(
                    ["--export", self.exportProgramInput.currentText()])
                currCommandNum = 2
            case "motion then audio":
                self.progressLabel.setText("Process 1 of 2")
                self.runAutoWProgressBar(motion_command)

                command = audio_command.copy()
                command[1] = "output.mp4"  # change input
                command[5] = f"{self.exportPath}"
                command.extend(
                    ["--export", self.exportProgramInput.currentText()])
                currCommandNum = 2
            case "keep both":  # default case is doing both at the same time
                command = default_both_command.copy()
                command.extend(
                    ["--export", self.exportProgramInput.currentText()])

        if (self.cutOrSplitInput.currentText() == "Split"):
            command.extend(["--silent-speed", "1", "--video-speed", "1"])

        if (self.silentInput1.value() > 0.00 or self.silentInput2.value() > 0.00):
            command.extend(["--margin",
                            f"{self.silentInput1.value()}s,"
                            f"{self.silentInput2.value()}s"])

        self.progressLabel.setText(
            f"Process {currCommandNum} of {currCommandNum}")

        self.runAutoWProgressBar(command)

# progress bar stuff
    def runAutoWProgressBar(self, command):
        # Reset the progress bar
        self.progressBar.reset()

        # Add PYTHONUNBUFFERED to environment variables for unbuffered output
        env = {**subprocess.os.environ, "PYTHONUNBUFFERED": "1"}

        # Run auto-editor as a subprocess
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            env=env,
            bufsize=1
        )

        pattern = r"\s+&.*\[\S+\]\s+(\d+\.\d+)%"

        for line in iter(process.stdout.readline, ""):
            if not line.strip():  # Skip empty lines
                continue
            # comment this out when i figure out threading
            print(f"Line: {line.strip()}")

            match = re.match(pattern, line)
            if match:
                progress = float(match.group(1))  # Extract percentage
                self.progressBar.setValue(progress)  # Update progress bar
            if "Finished." in line:
                self.progressBar.setValue(100)
                self.progressLabel.setText(line)
                print(command)

        process.wait()
        stderr = process.stderr.read().strip()  # Read all stderr after completion
        if stderr:
            print(stderr)
            self.progressLabel.setText(stderr)
