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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(548, 328)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_13 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.hiAudioLabel = QLabel(self.centralwidget)
        self.hiAudioLabel.setObjectName(u"hiAudioLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hiAudioLabel.sizePolicy().hasHeightForWidth())
        self.hiAudioLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.hiAudioLabel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.peakHiLabel = QLabel(self.centralwidget)
        self.peakHiLabel.setObjectName(u"peakHiLabel")
        sizePolicy.setHeightForWidth(self.peakHiLabel.sizePolicy().hasHeightForWidth())
        self.peakHiLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.peakHiLabel)

        self.peak_hi_DBValue = QLabel(self.centralwidget)
        self.peak_hi_DBValue.setObjectName(u"peak_hi_DBValue")
        sizePolicy.setHeightForWidth(self.peak_hi_DBValue.sizePolicy().hasHeightForWidth())
        self.peak_hi_DBValue.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.peak_hi_DBValue)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minHiLabel = QLabel(self.centralwidget)
        self.minHiLabel.setObjectName(u"minHiLabel")
        sizePolicy.setHeightForWidth(self.minHiLabel.sizePolicy().hasHeightForWidth())
        self.minHiLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.minHiLabel)

        self.min_hi_DBValue = QLabel(self.centralwidget)
        self.min_hi_DBValue.setObjectName(u"min_hi_DBValue")
        sizePolicy.setHeightForWidth(self.min_hi_DBValue.sizePolicy().hasHeightForWidth())
        self.min_hi_DBValue.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.min_hi_DBValue)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rmsHiLabel = QLabel(self.centralwidget)
        self.rmsHiLabel.setObjectName(u"rmsHiLabel")
        sizePolicy.setHeightForWidth(self.rmsHiLabel.sizePolicy().hasHeightForWidth())
        self.rmsHiLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.rmsHiLabel)

        self.rms_hi_DBValue = QLabel(self.centralwidget)
        self.rms_hi_DBValue.setObjectName(u"rms_hi_DBValue")
        sizePolicy.setHeightForWidth(self.rms_hi_DBValue.sizePolicy().hasHeightForWidth())
        self.rms_hi_DBValue.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.rms_hi_DBValue)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.audioLabel = QLabel(self.centralwidget)
        self.audioLabel.setObjectName(u"audioLabel")
        sizePolicy.setHeightForWidth(self.audioLabel.sizePolicy().hasHeightForWidth())
        self.audioLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.audioLabel)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.playheadVolumeLabel = QLabel(self.centralwidget)
        self.playheadVolumeLabel.setObjectName(u"playheadVolumeLabel")
        sizePolicy.setHeightForWidth(self.playheadVolumeLabel.sizePolicy().hasHeightForWidth())
        self.playheadVolumeLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.playheadVolumeLabel)

        self.playhead_DBValue = QLabel(self.centralwidget)
        self.playhead_DBValue.setObjectName(u"playhead_DBValue")
        sizePolicy.setHeightForWidth(self.playhead_DBValue.sizePolicy().hasHeightForWidth())
        self.playhead_DBValue.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.playhead_DBValue)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.peakLabel = QLabel(self.centralwidget)
        self.peakLabel.setObjectName(u"peakLabel")
        sizePolicy.setHeightForWidth(self.peakLabel.sizePolicy().hasHeightForWidth())
        self.peakLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.peakLabel)

        self.peak_DBValue = QLabel(self.centralwidget)
        self.peak_DBValue.setObjectName(u"peak_DBValue")
        sizePolicy.setHeightForWidth(self.peak_DBValue.sizePolicy().hasHeightForWidth())
        self.peak_DBValue.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.peak_DBValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.minLabel = QLabel(self.centralwidget)
        self.minLabel.setObjectName(u"minLabel")
        sizePolicy.setHeightForWidth(self.minLabel.sizePolicy().hasHeightForWidth())
        self.minLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.minLabel)

        self.min_DBValue = QLabel(self.centralwidget)
        self.min_DBValue.setObjectName(u"min_DBValue")
        sizePolicy.setHeightForWidth(self.min_DBValue.sizePolicy().hasHeightForWidth())
        self.min_DBValue.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.min_DBValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.rmsLabel = QLabel(self.centralwidget)
        self.rmsLabel.setObjectName(u"rmsLabel")
        sizePolicy.setHeightForWidth(self.rmsLabel.sizePolicy().hasHeightForWidth())
        self.rmsLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.rmsLabel)

        self.rms_DBValue = QLabel(self.centralwidget)
        self.rms_DBValue.setObjectName(u"rms_DBValue")
        sizePolicy.setHeightForWidth(self.rms_DBValue.sizePolicy().hasHeightForWidth())
        self.rms_DBValue.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.rms_DBValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout_13.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.silentPadLabel = QLabel(self.centralwidget)
        self.silentPadLabel.setObjectName(u"silentPadLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.silentPadLabel.sizePolicy().hasHeightForWidth())
        self.silentPadLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_7.addWidget(self.silentPadLabel)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.silentInput1 = QSpinBox(self.centralwidget)
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

        self.silentInput2 = QSpinBox(self.centralwidget)
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

        self.verticalSpacer = QSpacerItem(14, 22, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

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

        self.horizontalLayout_11.addWidget(self.audioCutInput)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)


        self.verticalLayout_6.addLayout(self.verticalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(14, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

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


        self.horizontalLayout_13.addLayout(self.verticalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 548, 33))
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

        self.exportButton.setDefault(True)
        self.clearButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.hiAudioLabel.setText(QCoreApplication.translate("MainWindow", u"Highlighted Section Audio Stats", None))
        self.peakHiLabel.setText(QCoreApplication.translate("MainWindow", u"Peak Level (db):", None))
        self.peak_hi_DBValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.minHiLabel.setText(QCoreApplication.translate("MainWindow", u"Min Level (db):", None))
        self.min_hi_DBValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rmsHiLabel.setText(QCoreApplication.translate("MainWindow", u"RMS Level (dB): ", None))
        self.rms_hi_DBValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.audioLabel.setText(QCoreApplication.translate("MainWindow", u"Overall Audio Stats", None))
        self.playheadVolumeLabel.setText(QCoreApplication.translate("MainWindow", u"Playhead Volume (dB):", None))
        self.playhead_DBValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.peakLabel.setText(QCoreApplication.translate("MainWindow", u"Peak Level (db):", None))
        self.peak_DBValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.minLabel.setText(QCoreApplication.translate("MainWindow", u"Min Level (db):", None))
        self.min_DBValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rmsLabel.setText(QCoreApplication.translate("MainWindow", u"RMS Level (dB): ", None))
        self.rms_DBValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.silentPadLabel.setText(QCoreApplication.translate("MainWindow", u"Silent padding margin ", None))
        self.splitLabel.setText(QCoreApplication.translate("MainWindow", u"split", None))
        self.uniform_checkbox.setText(QCoreApplication.translate("MainWindow", u"Uniform", None))
        self.autoLabel.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.cutOrSplitInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Cut Out", None))
        self.cutOrSplitInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Split", None))

        self.motionlessLabel.setText(QCoreApplication.translate("MainWindow", u"Motionless", None))
        self.audioCutLabel.setText(QCoreApplication.translate("MainWindow", u"Audio below", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi
