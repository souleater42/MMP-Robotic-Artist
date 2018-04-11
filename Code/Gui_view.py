# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Robotic_Artist_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.setEnabled(True)
        mainWindow.resize(950, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(950, 600))
        mainWindow.setMaximumSize(QtCore.QSize(950, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        mainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/MMP-Robotic-Artist/Code/Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setWindowOpacity(1.0)
        mainWindow.setDockNestingEnabled(False)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.MainView = QtWidgets.QWidget(mainWindow)
        self.MainView.setAutoFillBackground(False)
        self.MainView.setStyleSheet("background-color: rgb(199, 199, 231);")
        self.MainView.setObjectName("MainView")
        self.layoutWidget = QtWidgets.QWidget(self.MainView)
        self.layoutWidget.setGeometry(QtCore.QRect(-10, 0, 956, 602))
        self.layoutWidget.setObjectName("layoutWidget")
        self.base_layer = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.base_layer.setContentsMargins(0, 0, 0, 0)
        self.base_layer.setObjectName("base_layer")
        self.description_layer = QtWidgets.QVBoxLayout()
        self.description_layer.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.description_layer.setContentsMargins(20, 5, 0, -1)
        self.description_layer.setObjectName("description_layer")
        self.Title = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        self.Title.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typewriter")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setMouseTracking(True)
        self.Title.setStyleSheet("background-color: rgb(247, 23, 23);\n"
"border-right-color: rgb(247, 23, 23);\n"
"border-top-color: rgb(247, 23, 23);\n"
"border-bottom-color: rgb(30, 27, 24);\n"
"")
        self.Title.setFrameShape(QtWidgets.QFrame.Box)
        self.Title.setLineWidth(3)
        self.Title.setObjectName("Title")
        self.description_layer.addWidget(self.Title)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.description_layer.addItem(spacerItem)
        self.sub_title = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sub_title.sizePolicy().hasHeightForWidth())
        self.sub_title.setSizePolicy(sizePolicy)
        self.sub_title.setMinimumSize(QtCore.QSize(400, 0))
        self.sub_title.setObjectName("sub_title")
        self.description_layer.addWidget(self.sub_title)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.description_layer.addItem(spacerItem1)
        self.description_text = QtWidgets.QTextBrowser(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description_text.sizePolicy().hasHeightForWidth())
        self.description_text.setSizePolicy(sizePolicy)
        self.description_text.setMinimumSize(QtCore.QSize(400, 0))
        self.description_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.description_text.setObjectName("description_text")
        self.description_layer.addWidget(self.description_text)
        self.base_layer.addLayout(self.description_layer)
        self.line_separator = QtWidgets.QFrame(self.layoutWidget)
        self.line_separator.setWindowModality(QtCore.Qt.NonModal)
        self.line_separator.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_separator.setLineWidth(3)
        self.line_separator.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_separator.setObjectName("line_separator")
        self.base_layer.addWidget(self.line_separator)
        self.page_layer = QtWidgets.QStackedWidget(self.layoutWidget)
        self.page_layer.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_layer.sizePolicy().hasHeightForWidth())
        self.page_layer.setSizePolicy(sizePolicy)
        self.page_layer.setMinimumSize(QtCore.QSize(500, 600))
        self.page_layer.setObjectName("page_layer")
        self.Video_Capture = QtWidgets.QWidget()
        self.Video_Capture.setObjectName("Video_Capture")
        self.layoutWidget1 = QtWidgets.QWidget(self.Video_Capture)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 20, 491, 511))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.display_layer1 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.display_layer1.setContentsMargins(0, 0, 0, 0)
        self.display_layer1.setObjectName("display_layer1")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.display_layer1.addItem(spacerItem2)
        self.video_capture = QtWidgets.QLabel(self.layoutWidget1)
        self.video_capture.setMinimumSize(QtCore.QSize(300, 300))
        self.video_capture.setObjectName("video_capture")
        self.display_layer1.addWidget(self.video_capture)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.display_layer1.addItem(spacerItem3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.check_process = QtWidgets.QCheckBox(self.layoutWidget1)
        self.check_process.setObjectName("check_process")
        self.gridLayout.addWidget(self.check_process, 0, 0, 1, 1)
        self.check_use_after = QtWidgets.QCheckBox(self.layoutWidget1)
        self.check_use_after.setObjectName("check_use_after")
        self.gridLayout.addWidget(self.check_use_after, 1, 0, 1, 1)
        self.capture_picture = QtWidgets.QPushButton(self.layoutWidget1)
        self.capture_picture.setObjectName("capture_picture")
        self.gridLayout.addWidget(self.capture_picture, 2, 0, 1, 1)
        self.display_layer1.addLayout(self.gridLayout)
        self.page_layer.addWidget(self.Video_Capture)
        self.picture_display = QtWidgets.QWidget()
        self.picture_display.setObjectName("picture_display")
        self.layoutWidget2 = QtWidgets.QWidget(self.picture_display)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 20, 491, 511))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.display_layer2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.display_layer2.setContentsMargins(0, 0, 0, 0)
        self.display_layer2.setObjectName("display_layer2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.display_layer2.addItem(spacerItem4)
        self.captured_image = QtWidgets.QLabel(self.layoutWidget2)
        self.captured_image.setMinimumSize(QtCore.QSize(300, 300))
        self.captured_image.setObjectName("captured_image")
        self.display_layer2.addWidget(self.captured_image)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.display_layer2.addItem(spacerItem5)
        self.question_field = QtWidgets.QVBoxLayout()
        self.question_field.setObjectName("question_field")
        self.question1 = QtWidgets.QLabel(self.layoutWidget2)
        self.question1.setObjectName("question1")
        self.question_field.addWidget(self.question1)
        self.yes_no_field = QtWidgets.QHBoxLayout()
        self.yes_no_field.setObjectName("yes_no_field")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.yes_no_field.addItem(spacerItem6)
        self.yes_no_button = QtWidgets.QDialogButtonBox(self.layoutWidget2)
        self.yes_no_button.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.yes_no_button.setObjectName("yes_no_button")
        self.yes_no_field.addWidget(self.yes_no_button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.yes_no_field.addItem(spacerItem7)
        self.question_field.addLayout(self.yes_no_field)
        self.display_layer2.addLayout(self.question_field)
        self.page_layer.addWidget(self.picture_display)
        self.Style_Selection = QtWidgets.QWidget()
        self.Style_Selection.setObjectName("Style_Selection")
        self.btn_continue1 = QtWidgets.QPushButton(self.Style_Selection)
        self.btn_continue1.setGeometry(QtCore.QRect(200, 430, 99, 27))
        self.btn_continue1.setObjectName("btn_continue1")
        self.layoutWidget3 = QtWidgets.QWidget(self.Style_Selection)
        self.layoutWidget3.setGeometry(QtCore.QRect(40, 40, 422, 318))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.displayer_layer3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.displayer_layer3.setContentsMargins(0, 0, 0, 0)
        self.displayer_layer3.setObjectName("displayer_layer3")
        self.label_select_statement = QtWidgets.QLabel(self.layoutWidget3)
        self.label_select_statement.setObjectName("label_select_statement")
        self.displayer_layer3.addWidget(self.label_select_statement)
        self.Image_selection_layer = QtWidgets.QGridLayout()
        self.Image_selection_layer.setObjectName("Image_selection_layer")
        self.image_your_picture = QtWidgets.QLabel(self.layoutWidget3)
        self.image_your_picture.setMinimumSize(QtCore.QSize(100, 100))
        self.image_your_picture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_your_picture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_your_picture.setLineWidth(5)
        self.image_your_picture.setObjectName("image_your_picture")
        self.Image_selection_layer.addWidget(self.image_your_picture, 0, 0, 1, 1)
        self.image_style1 = QtWidgets.QLabel(self.layoutWidget3)
        self.image_style1.setMinimumSize(QtCore.QSize(100, 100))
        self.image_style1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_style1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_style1.setLineWidth(5)
        self.image_style1.setObjectName("image_style1")
        self.Image_selection_layer.addWidget(self.image_style1, 0, 1, 1, 1)
        self.image_style2 = QtWidgets.QLabel(self.layoutWidget3)
        self.image_style2.setMinimumSize(QtCore.QSize(100, 100))
        self.image_style2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_style2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_style2.setLineWidth(5)
        self.image_style2.setObjectName("image_style2")
        self.Image_selection_layer.addWidget(self.image_style2, 0, 2, 1, 1)
        self.image_style3 = QtWidgets.QLabel(self.layoutWidget3)
        self.image_style3.setMinimumSize(QtCore.QSize(100, 100))
        self.image_style3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_style3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_style3.setLineWidth(5)
        self.image_style3.setObjectName("image_style3")
        self.Image_selection_layer.addWidget(self.image_style3, 0, 3, 1, 1)
        self.label_your_picture = QtWidgets.QLabel(self.layoutWidget3)
        self.label_your_picture.setObjectName("label_your_picture")
        self.Image_selection_layer.addWidget(self.label_your_picture, 1, 0, 1, 1)
        self.check_style1 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.check_style1.setObjectName("check_style1")
        self.Image_selection_layer.addWidget(self.check_style1, 1, 1, 1, 1)
        self.check_style2 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.check_style2.setObjectName("check_style2")
        self.Image_selection_layer.addWidget(self.check_style2, 1, 2, 1, 1)
        self.check_style3 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.check_style3.setObjectName("check_style3")
        self.Image_selection_layer.addWidget(self.check_style3, 1, 3, 1, 1)
        self.image_style4 = QtWidgets.QLabel(self.layoutWidget3)
        self.image_style4.setMinimumSize(QtCore.QSize(100, 100))
        self.image_style4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_style4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_style4.setLineWidth(5)
        self.image_style4.setObjectName("image_style4")
        self.Image_selection_layer.addWidget(self.image_style4, 2, 0, 1, 1)
        self.image_style5 = QtWidgets.QLabel(self.layoutWidget3)
        self.image_style5.setMinimumSize(QtCore.QSize(100, 100))
        self.image_style5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_style5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_style5.setLineWidth(5)
        self.image_style5.setObjectName("image_style5")
        self.Image_selection_layer.addWidget(self.image_style5, 2, 1, 1, 1)
        self.check_style4 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.check_style4.setObjectName("check_style4")
        self.Image_selection_layer.addWidget(self.check_style4, 3, 0, 1, 1)
        self.check_style5 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.check_style5.setObjectName("check_style5")
        self.Image_selection_layer.addWidget(self.check_style5, 3, 1, 1, 1)
        self.displayer_layer3.addLayout(self.Image_selection_layer)
        self.page_layer.addWidget(self.Style_Selection)
        self.Print_Confirmation = QtWidgets.QWidget()
        self.Print_Confirmation.setObjectName("Print_Confirmation")
        self.layoutWidget_2 = QtWidgets.QWidget(self.Print_Confirmation)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 20, 491, 511))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.display_layer4 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.display_layer4.setContentsMargins(0, 0, 0, 0)
        self.display_layer4.setObjectName("display_layer4")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.display_layer4.addItem(spacerItem8)
        self.styled_image = QtWidgets.QLabel(self.layoutWidget_2)
        self.styled_image.setMinimumSize(QtCore.QSize(300, 300))
        self.styled_image.setObjectName("styled_image")
        self.display_layer4.addWidget(self.styled_image)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.display_layer4.addItem(spacerItem9)
        self.question_field2 = QtWidgets.QVBoxLayout()
        self.question_field2.setObjectName("question_field2")
        self.label_question2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_question2.setObjectName("label_question2")
        self.question_field2.addWidget(self.label_question2)
        self.yes_no_field2 = QtWidgets.QHBoxLayout()
        self.yes_no_field2.setObjectName("yes_no_field2")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.yes_no_field2.addItem(spacerItem10)
        self.yes_no_button2 = QtWidgets.QDialogButtonBox(self.layoutWidget_2)
        self.yes_no_button2.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.yes_no_button2.setObjectName("yes_no_button2")
        self.yes_no_field2.addWidget(self.yes_no_button2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.yes_no_field2.addItem(spacerItem11)
        self.question_field2.addLayout(self.yes_no_field2)
        self.display_layer4.addLayout(self.question_field2)
        self.page_layer.addWidget(self.Print_Confirmation)
        self.base_layer.addWidget(self.page_layer)
        mainWindow.setCentralWidget(self.MainView)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 25))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAdmin = QtWidgets.QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit_Application = QtWidgets.QAction(mainWindow)
        self.actionExit_Application.setObjectName("actionExit_Application")
        self.actionLogin = QtWidgets.QAction(mainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionToggle_Admin_View = QtWidgets.QAction(mainWindow)
        self.actionToggle_Admin_View.setObjectName("actionToggle_Admin_View")
        self.actionTutorial = QtWidgets.QAction(mainWindow)
        self.actionTutorial.setObjectName("actionTutorial")
        self.menuHelp.addAction(self.actionTutorial)
        self.menuAdmin.addAction(self.actionLogin)
        self.menuAdmin.addSeparator()
        self.menuAdmin.addAction(self.actionToggle_Admin_View)
        self.menuFile.addAction(self.actionExit_Application)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        self.page_layer.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Robotic Artist : Walter"))
        self.Title.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Robotic Artist : Walter</p></body></html>"))
        self.sub_title.setText(_translate("mainWindow", "Description:"))
        self.description_text.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this is where my project description will go. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.video_capture.setText(_translate("mainWindow", "This is where the video feed will go"))
        self.check_process.setText(_translate("mainWindow", "Tick to allow photos to be processed in this app"))
        self.check_use_after.setText(_translate("mainWindow", "Allow images to be used for testing or presentation purposes"))
        self.capture_picture.setText(_translate("mainWindow", "Capture Picture"))
        self.captured_image.setText(_translate("mainWindow", "This is where the picture that was taken will be displayed"))
        self.question1.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Is this the picture  you would like to use?</p></body></html>"))
        self.btn_continue1.setText(_translate("mainWindow", "Continue"))
        self.label_select_statement.setText(_translate("mainWindow", "<html><head/><body><p>Please select style: </p><p>(select image for the one you want)</p></body></html>"))
        self.image_your_picture.setText(_translate("mainWindow", "<html><head/><body><p><br/></p><p>Image</p></body></html>"))
        self.image_style1.setText(_translate("mainWindow", "<html><head/><body><p><br/></p><p>Image</p></body></html>"))
        self.image_style2.setText(_translate("mainWindow", "<html><head/><body><p><br/></p><p>Image</p></body></html>"))
        self.image_style3.setText(_translate("mainWindow", "<html><head/><body><p><br/></p><p>Image</p></body></html>"))
        self.label_your_picture.setText(_translate("mainWindow", "Your Picture"))
        self.check_style1.setText(_translate("mainWindow", "Style 1"))
        self.check_style2.setText(_translate("mainWindow", "Style 2"))
        self.check_style3.setText(_translate("mainWindow", "Style 3"))
        self.image_style4.setText(_translate("mainWindow", "<html><head/><body><p><br/></p><p>Image</p></body></html>"))
        self.image_style5.setText(_translate("mainWindow", "<html><head/><body><p><br/></p><p>Image</p></body></html>"))
        self.check_style4.setText(_translate("mainWindow", "Style 4"))
        self.check_style5.setText(_translate("mainWindow", "Style 5"))
        self.styled_image.setText(_translate("mainWindow", "This is where the picture that was processed will be displayed"))
        self.label_question2.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Is this the style that you would like?</p></body></html>"))
        self.menuHelp.setTitle(_translate("mainWindow", "Help"))
        self.menuAdmin.setTitle(_translate("mainWindow", "Admin"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.actionExit_Application.setText(_translate("mainWindow", "Exit Application"))
        self.actionLogin.setText(_translate("mainWindow", "Login"))
        self.actionToggle_Admin_View.setText(_translate("mainWindow", "Toggle Admin View"))
        self.actionTutorial.setText(_translate("mainWindow", "Tutorial"))

import Resources_rc