from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(987, 715)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(78, 0, 104)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(78, 0, 104)")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("background-color: white; border-radius: 10px; ")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horLay1 = QtWidgets.QHBoxLayout()
        self.horLay1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horLay1.setContentsMargins(0, 0, 0, -1)
        self.horLay1.setSpacing(0)
        self.horLay1.setObjectName("horLay1")
        self.check_class = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(35)
        sizePolicy.setHeightForWidth(self.check_class.sizePolicy().hasHeightForWidth())
        self.check_class.setSizePolicy(sizePolicy)
        self.check_class.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.check_class.setFont(font)
        self.check_class.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.check_class.setObjectName("check_class")
        self.horLay1.addWidget(self.check_class)
        self.label = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horLay1.addWidget(self.label)
        self.class_box = QtWidgets.QComboBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class_box.sizePolicy().hasHeightForWidth())
        self.class_box.setSizePolicy(sizePolicy)
        self.class_box.setMinimumSize(QtCore.QSize(0, 35))
        self.class_box.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.class_box.setFont(font)
        self.class_box.setStyleSheet("QComboBox {\n"
"border-left: 2px solid black;\n"
"border-top: 2px solid black;\n"
"border-bottom: 2px solid black;\n"
"border-right: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"   border-left: 2px solid black;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"   image: url(./static/arrow_down_1.png)\n"
"}")
        self.class_box.setObjectName("class_box")
        self.horLay1.addWidget(self.class_box)
        self.class_lab = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class_lab.sizePolicy().hasHeightForWidth())
        self.class_lab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.class_lab.setFont(font)
        self.class_lab.setLineWidth(1)
        self.class_lab.setObjectName("class_lab")
        self.horLay1.addWidget(self.class_lab)
        self.subject_box = QtWidgets.QComboBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subject_box.sizePolicy().hasHeightForWidth())
        self.subject_box.setSizePolicy(sizePolicy)
        self.subject_box.setMaximumSize(QtCore.QSize(16000000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.subject_box.setFont(font)
        self.subject_box.setStyleSheet("QComboBox {\n"
"border-left: 2px solid black;\n"
"border-top: 2px solid black;\n"
"border-bottom: 2px solid black;\n"
"border-right: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"   border-left: 2px solid black;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"   image: url(./static/arrow_down_1.png)\n"
"}")
        self.subject_box.setObjectName("subject_box")
        self.horLay1.addWidget(self.subject_box)
        self.verticalLayout_3.addLayout(self.horLay1)
        self.horLay3 = QtWidgets.QHBoxLayout()
        self.horLay3.setObjectName("horLay3")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horLay3.addWidget(self.label_3)
        self.start_date = QtWidgets.QDateEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(35)
        sizePolicy.setHeightForWidth(self.start_date.sizePolicy().hasHeightForWidth())
        self.start_date.setSizePolicy(sizePolicy)
        self.start_date.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.start_date.setFont(font)
        self.start_date.setAutoFillBackground(False)
        self.start_date.setStyleSheet("QDateEdit {\n"
"border-left: 2px solid black;\n"
"border-top: 2px solid black;\n"
"border-right: 2px solid black;\n"
"border-bottom: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"color: black;\n"
"font-color: black;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"   border-left: 2px solid black;\n"
"}\n"
"\n"
"QDateEdit::QCalendarWidget {\n"
"background-color: rgb(211, 78, 255);\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"   image: url(./static/arrow_down_1.png)\n"
"}r")
        self.start_date.setWrapping(False)
        self.start_date.setProperty("showGroupSeparator", False)
        self.start_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 9, 1), QtCore.QTime(0, 0, 0)))
        self.start_date.setCalendarPopup(True)
        self.start_date.setObjectName("start_date")
        self.horLay3.addWidget(self.start_date)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horLay3.addWidget(self.label_4)
        self.finish_date = QtWidgets.QDateEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(35)
        sizePolicy.setHeightForWidth(self.finish_date.sizePolicy().hasHeightForWidth())
        self.finish_date.setSizePolicy(sizePolicy)
        self.finish_date.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.finish_date.setFont(font)
        self.finish_date.setStyleSheet("QDateEdit {\n"
"border-left: 2px solid black;\n"
"border-top: 2px solid black;\n"
"border-right: 2px solid black;\n"
"border-bottom: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"color: black;\n"
"font-color: black;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"   border-left: 2px solid black;\n"
"}\n"
"\n"
"QDateEdit::QCalendarWidget {\n"
"background-color: rgb(211, 78, 255);\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"   image: url(./static/arrow_down_1.png)\n"
"}r")
        self.finish_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 10, 1), QtCore.QTime(0, 0, 0)))
        self.finish_date.setCalendarPopup(True)
        self.finish_date.setObjectName("finish_date")
        self.horLay3.addWidget(self.finish_date)
        self.month_ago = QtWidgets.QPushButton(self.widget_2)
        self.month_ago.setMinimumSize(QtCore.QSize(0, 35))
        self.month_ago.setMaximumSize(QtCore.QSize(30, 100))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.month_ago.setFont(font)
        self.month_ago.setToolTip("")
        self.month_ago.setWhatsThis("")
        self.month_ago.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.month_ago.setAutoDefault(False)
        self.month_ago.setObjectName("month_ago")
        self.horLay3.addWidget(self.month_ago)
        self.month_later = QtWidgets.QPushButton(self.widget_2)
        self.month_later.setMinimumSize(QtCore.QSize(0, 35))
        self.month_later.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.month_later.setFont(font)
        self.month_later.setToolTip("")
        self.month_later.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.month_later.setObjectName("month_later")
        self.horLay3.addWidget(self.month_later)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.horLay3.addWidget(self.widget_5)
        self.verticalLayout_3.addLayout(self.horLay3)
        self.horLay2 = QtWidgets.QHBoxLayout()
        self.horLay2.setObjectName("horLay2")
        self.pupil_name_for_find = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pupil_name_for_find.sizePolicy().hasHeightForWidth())
        self.pupil_name_for_find.setSizePolicy(sizePolicy)
        self.pupil_name_for_find.setMinimumSize(QtCore.QSize(600, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pupil_name_for_find.setFont(font)
        self.pupil_name_for_find.setStyleSheet("border-radius: 5px;\n"
"background-color: white;\n"
"border: 2px solid black;")
        self.pupil_name_for_find.setObjectName("pupil_name_for_find")
        self.horLay2.addWidget(self.pupil_name_for_find)
        self.btn_find_pupil = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_find_pupil.sizePolicy().hasHeightForWidth())
        self.btn_find_pupil.setSizePolicy(sizePolicy)
        self.btn_find_pupil.setMinimumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_find_pupil.setFont(font)
        self.btn_find_pupil.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_find_pupil.setObjectName("btn_find_pupil")
        self.horLay2.addWidget(self.btn_find_pupil)
        self.verticalLayout_3.addLayout(self.horLay2)
        self.error_lab = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.error_lab.setFont(font)
        self.error_lab.setObjectName("error_lab")
        self.verticalLayout_3.addWidget(self.error_lab)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setStyleSheet("background-color: white; border-radius: 10px")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.table_puplis = QtWidgets.QTableWidget(self.widget_4)
        self.table_puplis.setStyleSheet("")
        self.table_puplis.setDragEnabled(False)
        self.table_puplis.setShowGrid(True)
        self.table_puplis.setGridStyle(QtCore.Qt.SolidLine)
        self.table_puplis.setCornerButtonEnabled(True)
        self.table_puplis.setObjectName("table_puplis")
        self.table_puplis.setColumnCount(0)
        self.table_puplis.setRowCount(0)
        self.table_puplis.horizontalHeader().setVisible(True)
        self.table_puplis.horizontalHeader().setCascadingSectionResizes(False)
        self.table_puplis.horizontalHeader().setHighlightSections(True)
        self.table_puplis.horizontalHeader().setSortIndicatorShown(True)
        self.table_puplis.horizontalHeader().setStretchLastSection(False)
        self.table_puplis.verticalHeader().setVisible(True)
        self.table_puplis.verticalHeader().setCascadingSectionResizes(False)
        self.table_puplis.verticalHeader().setHighlightSections(True)
        self.table_puplis.verticalHeader().setSortIndicatorShown(False)
        self.table_puplis.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.table_puplis)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("background-color: white; border-radius: 10px;")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horLay_5 = QtWidgets.QHBoxLayout()
        self.horLay_5.setObjectName("horLay_5")
        self.btn_sort = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sort.sizePolicy().hasHeightForWidth())
        self.btn_sort.setSizePolicy(sizePolicy)
        self.btn_sort.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_sort.setFont(font)
        self.btn_sort.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_sort.setAutoDefault(True)
        self.btn_sort.setObjectName("btn_sort")
        self.horLay_5.addWidget(self.btn_sort)
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horLay_5.addWidget(self.label_5)
        self.sort_key_box = QtWidgets.QComboBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sort_key_box.sizePolicy().hasHeightForWidth())
        self.sort_key_box.setSizePolicy(sizePolicy)
        self.sort_key_box.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sort_key_box.setFont(font)
        self.sort_key_box.setStyleSheet("QComboBox {\n"
"border-left: 2px solid black;\n"
"border-top: 2px solid black;\n"
"border-bottom: 2px solid black;\n"
"border-right: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"   border-left: 2px solid black;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"   image: url(./static/arrow_down_1.png)\n"
"}")
        self.sort_key_box.setObjectName("sort_key_box")
        self.sort_key_box.addItem("")
        self.sort_key_box.addItem("")
        self.sort_key_box.addItem("")
        self.horLay_5.addWidget(self.sort_key_box)
        self.sort_order = QtWidgets.QPushButton(self.widget_3)
        self.sort_order.setMinimumSize(QtCore.QSize(0, 35))
        self.sort_order.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sort_order.setFont(font)
        self.sort_order.setToolTip("По возрастанию")
        self.sort_order.setStatusTip("")
        self.sort_order.setWhatsThis("")
        self.sort_order.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.sort_order.setObjectName("sort_order")
        self.horLay_5.addWidget(self.sort_order)
        self.verticalLayout_4.addLayout(self.horLay_5)
        self.horLay4 = QtWidgets.QHBoxLayout()
        self.horLay4.setObjectName("horLay4")
        self.btn_delete_pupil = QtWidgets.QPushButton(self.widget_3)
        self.btn_delete_pupil.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_delete_pupil.setFont(font)
        self.btn_delete_pupil.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_delete_pupil.setObjectName("btn_delete_pupil")
        self.horLay4.addWidget(self.btn_delete_pupil)
        self.btn_add_pupil = QtWidgets.QPushButton(self.widget_3)
        self.btn_add_pupil.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_add_pupil.setFont(font)
        self.btn_add_pupil.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_add_pupil.setObjectName("btn_add_pupil")
        self.horLay4.addWidget(self.btn_add_pupil)
        self.btn_open_pupil = QtWidgets.QPushButton(self.widget_3)
        self.btn_open_pupil.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_open_pupil.setFont(font)
        self.btn_open_pupil.setStyleSheet("QPushButton {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.btn_open_pupil.setObjectName("btn_open_pupil")
        self.horLay4.addWidget(self.btn_open_pupil)
        self.verticalLayout_4.addLayout(self.horLay4)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 987, 26))
        self.menuBar.setStyleSheet("background-color: white; \n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px")
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setAutoFillBackground(False)
        self.menu.setStyleSheet("QMenu {color: black;}\n"
"QMenu::selected {background-color: lightgray;}")
        self.menu.setSeparatorsCollapsible(False)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setStyleSheet("QMenu {color: black;}\n"
"QMenu::selected {background-color: lightgray;}")
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        self.statusBar.setMaximumSize(QtCore.QSize(16777215, 15))
        self.statusBar.setStyleSheet("background-color: white;\n"
"height: 10px")
        self.statusBar.setSizeGripEnabled(True)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.about_programm_action = QtWidgets.QAction(MainWindow)
        self.about_programm_action.setObjectName("about_programm_action")
        self.create_bd_action = QtWidgets.QAction(MainWindow)
        self.create_bd_action.setObjectName("create_bd_action")
        self.help_action = QtWidgets.QAction(MainWindow)
        self.help_action.setObjectName("help_action")
        self.add_subject_action = QtWidgets.QAction(MainWindow)
        self.add_subject_action.setObjectName("add_subject_action")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName("about_action")
        self.menu.addAction(self.add_subject_action)
        self.menuBar.addAction(self.menu.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.check_class.setText(_translate("MainWindow", "Показать"))
        self.label.setText(_translate("MainWindow", " КЛАСС: "))
        self.class_lab.setText(_translate("MainWindow", " ПРЕДМЕТ: "))
        self.label_3.setText(_translate("MainWindow", "C"))
        self.start_date.setDisplayFormat(_translate("MainWindow", "dd-MM-yyyy"))
        self.label_4.setText(_translate("MainWindow", "ПО"))
        self.finish_date.setDisplayFormat(_translate("MainWindow", "dd-MM-yyyy"))
        self.month_ago.setText(_translate("MainWindow", "❰"))
        self.month_later.setText(_translate("MainWindow", "❱"))
        self.btn_find_pupil.setText(_translate("MainWindow", "Найти"))
        self.error_lab.setText(_translate("MainWindow", "Ученик не найден"))
        self.table_puplis.setSortingEnabled(True)
        self.btn_sort.setText(_translate("MainWindow", "Отсортировать"))
        self.label_5.setText(_translate("MainWindow", "по"))
        self.sort_key_box.setItemText(0, _translate("MainWindow", "id"))
        self.sort_key_box.setItemText(1, _translate("MainWindow", "ФИО"))
        self.sort_key_box.setItemText(2, _translate("MainWindow", "Средний бал"))
        self.sort_order.setText(_translate("MainWindow", "🠕"))
        self.btn_delete_pupil.setText(_translate("MainWindow", "Удалить ученика"))
        self.btn_delete_pupil.setShortcut(_translate("MainWindow", "Del"))
        self.btn_add_pupil.setText(_translate("MainWindow", "Добавить ученика"))
        self.btn_add_pupil.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.btn_open_pupil.setText(_translate("MainWindow", "Профиль ученика"))
        self.btn_open_pupil.setShortcut(_translate("MainWindow", "O"))
        self.menu.setTitle(_translate("MainWindow", "Дополнительно"))
        self.add_subject_action.setText(_translate("MainWindow", "Управление предметами"))
