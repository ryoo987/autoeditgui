# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_v1.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 346)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.fileInputBtn = QPushButton(self.centralwidget)
        self.fileInputBtn.setObjectName(u"fileInputBtn")

        self.verticalLayout_5.addWidget(self.fileInputBtn)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.audioStatsLabel = QLabel(self.centralwidget)
        self.audioStatsLabel.setObjectName(u"audioStatsLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioStatsLabel.sizePolicy().hasHeightForWidth())
        self.audioStatsLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.audioStatsLabel)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.meanVolLabel = QLabel(self.centralwidget)
        self.meanVolLabel.setObjectName(u"meanVolLabel")
        sizePolicy.setHeightForWidth(self.meanVolLabel.sizePolicy().hasHeightForWidth())
        self.meanVolLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.meanVolLabel)

        self.meanDBValue = QLabel(self.centralwidget)
        self.meanDBValue.setObjectName(u"meanDBValue")
        sizePolicy.setHeightForWidth(self.meanDBValue.sizePolicy().hasHeightForWidth())
        self.meanDBValue.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.meanDBValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.maxVolLabel = QLabel(self.centralwidget)
        self.maxVolLabel.setObjectName(u"maxVolLabel")
        sizePolicy.setHeightForWidth(self.maxVolLabel.sizePolicy().hasHeightForWidth())
        self.maxVolLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.maxVolLabel)

        self.maxDBValue = QLabel(self.centralwidget)
        self.maxDBValue.setObjectName(u"maxDBValue")
        sizePolicy.setHeightForWidth(self.maxDBValue.sizePolicy().hasHeightForWidth())
        self.maxDBValue.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.maxDBValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.playheadVolumeLabel = QLabel(self.centralwidget)
        self.playheadVolumeLabel.setObjectName(u"playheadVolumeLabel")
        sizePolicy.setHeightForWidth(self.playheadVolumeLabel.sizePolicy().hasHeightForWidth())
        self.playheadVolumeLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.playheadVolumeLabel)

        self.playheadDBValue = QLabel(self.centralwidget)
        self.playheadDBValue.setObjectName(u"playheadDBValue")
        sizePolicy.setHeightForWidth(self.playheadDBValue.sizePolicy().hasHeightForWidth())
        self.playheadDBValue.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.playheadDBValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.genDBInfo = QLabel(self.centralwidget)
        self.genDBInfo.setObjectName(u"genDBInfo")
        sizePolicy.setHeightForWidth(self.genDBInfo.sizePolicy().hasHeightForWidth())
        self.genDBInfo.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.genDBInfo)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.peakHiLabel = QLabel(self.centralwidget)
        self.peakHiLabel.setObjectName(u"peakHiLabel")
        sizePolicy.setHeightForWidth(self.peakHiLabel.sizePolicy().hasHeightForWidth())
        self.peakHiLabel.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.peakHiLabel)

        self.minHiLabel = QLabel(self.centralwidget)
        self.minHiLabel.setObjectName(u"minHiLabel")
        sizePolicy.setHeightForWidth(self.minHiLabel.sizePolicy().hasHeightForWidth())
        self.minHiLabel.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.minHiLabel)

        self.minHiLabel_2 = QLabel(self.centralwidget)
        self.minHiLabel_2.setObjectName(u"minHiLabel_2")
        sizePolicy.setHeightForWidth(self.minHiLabel_2.sizePolicy().hasHeightForWidth())
        self.minHiLabel_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.minHiLabel_2)

        self.minHiLabel_3 = QLabel(self.centralwidget)
        self.minHiLabel_3.setObjectName(u"minHiLabel_3")
        sizePolicy.setHeightForWidth(self.minHiLabel_3.sizePolicy().hasHeightForWidth())
        self.minHiLabel_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.minHiLabel_3)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.silentPadLabel = QLabel(self.centralwidget)
        self.silentPadLabel.setObjectName(u"silentPadLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.silentPadLabel.sizePolicy().hasHeightForWidth())
        self.silentPadLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_7.addWidget(self.silentPadLabel)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.silentInput1 = QDoubleSpinBox(self.centralwidget)
        self.silentInput1.setObjectName(u"silentInput1")
        sizePolicy.setHeightForWidth(self.silentInput1.sizePolicy().hasHeightForWidth())
        self.silentInput1.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.silentInput1)

        self.splitLabel = QLabel(self.centralwidget)
        self.splitLabel.setObjectName(u"splitLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.splitLabel.sizePolicy().hasHeightForWidth())
        self.splitLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.splitLabel)

        self.silentInput2 = QDoubleSpinBox(self.centralwidget)
        self.silentInput2.setObjectName(u"silentInput2")
        sizePolicy.setHeightForWidth(self.silentInput2.sizePolicy().hasHeightForWidth())
        self.silentInput2.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.silentInput2)

        self.uniform_checkbox = QCheckBox(self.centralwidget)
        self.uniform_checkbox.setObjectName(u"uniform_checkbox")
        self.uniform_checkbox.setChecked(True)

        self.horizontalLayout_8.addWidget(self.uniform_checkbox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)


        self.verticalLayout_6.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(14, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.autoLabel = QLabel(self.centralwidget)
        self.autoLabel.setObjectName(u"autoLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.autoLabel.sizePolicy().hasHeightForWidth())
        self.autoLabel.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.autoLabel)

        self.cutOrSplitInput = QComboBox(self.centralwidget)
        self.cutOrSplitInput.addItem("")
        self.cutOrSplitInput.addItem("")
        self.cutOrSplitInput.setObjectName(u"cutOrSplitInput")
        sizePolicy.setHeightForWidth(self.cutOrSplitInput.sizePolicy().hasHeightForWidth())
        self.cutOrSplitInput.setSizePolicy(sizePolicy)
        self.cutOrSplitInput.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.cutOrSplitInput)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.motionlessLabel = QLabel(self.centralwidget)
        self.motionlessLabel.setObjectName(u"motionlessLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.motionlessLabel.sizePolicy().hasHeightForWidth())
        self.motionlessLabel.setSizePolicy(sizePolicy4)

        self.horizontalLayout_10.addWidget(self.motionlessLabel)

        self.motionlessSliderInput = QSlider(self.centralwidget)
        self.motionlessSliderInput.setObjectName(u"motionlessSliderInput")
        sizePolicy.setHeightForWidth(self.motionlessSliderInput.sizePolicy().hasHeightForWidth())
        self.motionlessSliderInput.setSizePolicy(sizePolicy)
        self.motionlessSliderInput.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_10.addWidget(self.motionlessSliderInput)

        self.motionlessPercentInput = QSpinBox(self.centralwidget)
        self.motionlessPercentInput.setObjectName(u"motionlessPercentInput")
        sizePolicy.setHeightForWidth(self.motionlessPercentInput.sizePolicy().hasHeightForWidth())
        self.motionlessPercentInput.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.motionlessPercentInput)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.audioCutLabel = QLabel(self.centralwidget)
        self.audioCutLabel.setObjectName(u"audioCutLabel")

        self.horizontalLayout_11.addWidget(self.audioCutLabel)

        self.audioCutInput = QSpinBox(self.centralwidget)
        self.audioCutInput.setObjectName(u"audioCutInput")
        self.audioCutInput.setMinimum(-99)

        self.horizontalLayout_11.addWidget(self.audioCutInput)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)


        self.verticalLayout_6.addLayout(self.verticalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.editOrderLabel = QLabel(self.centralwidget)
        self.editOrderLabel.setObjectName(u"editOrderLabel")
        sizePolicy4.setHeightForWidth(self.editOrderLabel.sizePolicy().hasHeightForWidth())
        self.editOrderLabel.setSizePolicy(sizePolicy4)

        self.horizontalLayout_13.addWidget(self.editOrderLabel)

        self.editOrderInput = QComboBox(self.centralwidget)
        self.editOrderInput.addItem("")
        self.editOrderInput.addItem("")
        self.editOrderInput.addItem("")
        self.editOrderInput.addItem("")
        self.editOrderInput.addItem("")
        self.editOrderInput.setObjectName(u"editOrderInput")
        sizePolicy.setHeightForWidth(self.editOrderInput.sizePolicy().hasHeightForWidth())
        self.editOrderInput.setSizePolicy(sizePolicy)
        self.editOrderInput.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_13.addWidget(self.editOrderInput)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.exportProgramLabel = QLabel(self.centralwidget)
        self.exportProgramLabel.setObjectName(u"exportProgramLabel")

        self.horizontalLayout_14.addWidget(self.exportProgramLabel)

        self.exportProgramInput = QComboBox(self.centralwidget)
        self.exportProgramInput.addItem("")
        self.exportProgramInput.addItem("")
        self.exportProgramInput.addItem("")
        self.exportProgramInput.addItem("")
        self.exportProgramInput.addItem("")
        self.exportProgramInput.addItem("")
        self.exportProgramInput.setObjectName(u"exportProgramInput")
        sizePolicy.setHeightForWidth(self.exportProgramInput.sizePolicy().hasHeightForWidth())
        self.exportProgramInput.setSizePolicy(sizePolicy)
        self.exportProgramInput.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_14.addWidget(self.exportProgramInput)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_3 = QSpacerItem(91, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.exportButton = QPushButton(self.centralwidget)
        self.exportButton.setObjectName(u"exportButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.exportButton.sizePolicy().hasHeightForWidth())
        self.exportButton.setSizePolicy(sizePolicy5)

        self.horizontalLayout_12.addWidget(self.exportButton)

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setAutoDefault(False)
        self.clearButton.setFlat(False)

        self.horizontalLayout_12.addWidget(self.clearButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 550, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)

        self.fileInputBtn.setDefault(True)
        self.exportButton.setDefault(True)
        self.clearButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fileInputBtn.setText(QCoreApplication.translate("MainWindow", u"Import Video File", None))
        self.audioStatsLabel.setText(QCoreApplication.translate("MainWindow", u"Audio Stats", None))
        self.meanVolLabel.setText(QCoreApplication.translate("MainWindow", u"Mean Volume (db):", None))
        self.meanDBValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.maxVolLabel.setText(QCoreApplication.translate("MainWindow", u"Max Volume (db):", None))
        self.maxDBValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.playheadVolumeLabel.setText(QCoreApplication.translate("MainWindow", u"Playhead Volume (dB):", None))
        self.playheadDBValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.genDBInfo.setText(QCoreApplication.translate("MainWindow", u"General Db Info", None))
        self.peakHiLabel.setText(QCoreApplication.translate("MainWindow", u" 0 dB: Max loudness", None))
        self.minHiLabel.setText(QCoreApplication.translate("MainWindow", u"-25 dB: Speaking volume", None))
        self.minHiLabel_2.setText(QCoreApplication.translate("MainWindow", u"-50 dB: Soft bg noise", None))
        self.minHiLabel_3.setText(QCoreApplication.translate("MainWindow", u"-60 dB: Silence", None))
        self.silentPadLabel.setText(QCoreApplication.translate("MainWindow", u"Silent padding margin ", None))
        self.splitLabel.setText(QCoreApplication.translate("MainWindow", u"split", None))
        self.uniform_checkbox.setText(QCoreApplication.translate("MainWindow", u"Uniform", None))
        self.autoLabel.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.cutOrSplitInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Cut Out", None))
        self.cutOrSplitInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Split", None))

        self.motionlessLabel.setText(QCoreApplication.translate("MainWindow", u"Motionless", None))
        self.audioCutLabel.setText(QCoreApplication.translate("MainWindow", u"Audio below", None))
        self.editOrderLabel.setText(QCoreApplication.translate("MainWindow", u"Editing Order:", None))
        self.editOrderInput.setItemText(0, QCoreApplication.translate("MainWindow", u"audio only", None))
        self.editOrderInput.setItemText(1, QCoreApplication.translate("MainWindow", u"motion only", None))
        self.editOrderInput.setItemText(2, QCoreApplication.translate("MainWindow", u"audio then motion", None))
        self.editOrderInput.setItemText(3, QCoreApplication.translate("MainWindow", u"motion then audio", None))
        self.editOrderInput.setItemText(4, QCoreApplication.translate("MainWindow", u"keep both", None))

        self.exportProgramLabel.setText(QCoreApplication.translate("MainWindow", u"Export Program", None))
        self.exportProgramInput.setItemText(0, QCoreApplication.translate("MainWindow", u"default", None))
        self.exportProgramInput.setItemText(1, QCoreApplication.translate("MainWindow", u"premiere", None))
        self.exportProgramInput.setItemText(2, QCoreApplication.translate("MainWindow", u"resolve", None))
        self.exportProgramInput.setItemText(3, QCoreApplication.translate("MainWindow", u"shotcut", None))
        self.exportProgramInput.setItemText(4, QCoreApplication.translate("MainWindow", u"final-cut-pro", None))
        self.exportProgramInput.setItemText(5, QCoreApplication.translate("MainWindow", u"clip-sequence", None))

        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

