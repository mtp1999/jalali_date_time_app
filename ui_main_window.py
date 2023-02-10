# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setStyleSheet(u"#main_window{\n"
"	background-color: #eef6ec\n"
";\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #660033;\n"
"}")
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, 50, 50, 50)
        self.grid_layout_date = QGridLayout()
        self.grid_layout_date.setObjectName(u"grid_layout_date")
        self.label_date_value = QLabel(MainWindow)
        self.label_date_value.setObjectName(u"label_date_value")
        font = QFont()
        font.setPointSize(16)
        self.label_date_value.setFont(font)
        self.label_date_value.setAlignment(Qt.AlignCenter)

        self.grid_layout_date.addWidget(self.label_date_value, 0, 0, 1, 1)

        self.label_date = QLabel(MainWindow)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setFont(font)
        self.label_date.setMouseTracking(False)
        self.label_date.setLayoutDirection(Qt.LeftToRight)
        self.label_date.setAlignment(Qt.AlignCenter)
        self.label_date.setIndent(2)

        self.grid_layout_date.addWidget(self.label_date, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.grid_layout_date)

        self.grid_layout_year = QGridLayout()
        self.grid_layout_year.setObjectName(u"grid_layout_year")
        self.label_year_value = QLabel(MainWindow)
        self.label_year_value.setObjectName(u"label_year_value")
        self.label_year_value.setFont(font)
        self.label_year_value.setAlignment(Qt.AlignCenter)

        self.grid_layout_year.addWidget(self.label_year_value, 0, 0, 1, 1)

        self.label_year = QLabel(MainWindow)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setFont(font)
        self.label_year.setMouseTracking(False)
        self.label_year.setAlignment(Qt.AlignCenter)
        self.label_year.setIndent(2)

        self.grid_layout_year.addWidget(self.label_year, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.grid_layout_year)

        self.grid_layout_month = QGridLayout()
        self.grid_layout_month.setObjectName(u"grid_layout_month")
        self.label_month_value = QLabel(MainWindow)
        self.label_month_value.setObjectName(u"label_month_value")
        self.label_month_value.setFont(font)
        self.label_month_value.setFocusPolicy(Qt.ClickFocus)
        self.label_month_value.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_month_value.setAcceptDrops(False)
        self.label_month_value.setAlignment(Qt.AlignCenter)

        self.grid_layout_month.addWidget(self.label_month_value, 0, 0, 1, 1)

        self.label_month = QLabel(MainWindow)
        self.label_month.setObjectName(u"label_month")
        self.label_month.setFont(font)
        self.label_month.setMouseTracking(False)
        self.label_month.setStyleSheet(u"")
        self.label_month.setAlignment(Qt.AlignCenter)
        self.label_month.setIndent(2)

        self.grid_layout_month.addWidget(self.label_month, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.grid_layout_month)

        self.grid_layout_day = QGridLayout()
        self.grid_layout_day.setObjectName(u"grid_layout_day")
        self.label_day_value = QLabel(MainWindow)
        self.label_day_value.setObjectName(u"label_day_value")
        self.label_day_value.setFont(font)
        self.label_day_value.setAlignment(Qt.AlignCenter)

        self.grid_layout_day.addWidget(self.label_day_value, 0, 0, 1, 1)

        self.label_day = QLabel(MainWindow)
        self.label_day.setObjectName(u"label_day")
        self.label_day.setFont(font)
        self.label_day.setMouseTracking(False)
        self.label_day.setAlignment(Qt.AlignCenter)
        self.label_day.setIndent(2)

        self.grid_layout_day.addWidget(self.label_day, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.grid_layout_day)

        self.line1 = QFrame(MainWindow)
        self.line1.setObjectName(u"line1")
        self.line1.setStyleSheet(u"#line1{\n"
"	background-color: #d3d399;\n"
"\n"
"}")
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line1)

        self.grid_layout_time = QGridLayout()
        self.grid_layout_time.setObjectName(u"grid_layout_time")
        self.label_time_value = QLabel(MainWindow)
        self.label_time_value.setObjectName(u"label_time_value")
        self.label_time_value.setFont(font)
        self.label_time_value.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_time_value.setAlignment(Qt.AlignCenter)

        self.grid_layout_time.addWidget(self.label_time_value, 0, 0, 1, 1)

        self.label_time = QLabel(MainWindow)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setFont(font)
        self.label_time.setMouseTracking(False)
        self.label_time.setLayoutDirection(Qt.LeftToRight)
        self.label_time.setAlignment(Qt.AlignCenter)
        self.label_time.setIndent(2)

        self.grid_layout_time.addWidget(self.label_time, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.grid_layout_time)

        self.button_language = QPushButton(MainWindow)
        self.button_language.setObjectName(u"button_language")
        self.button_language.setFont(font)
        self.button_language.setStyleSheet(u"#button_language {\n"
"	background-color: #d3d399;\n"
"	color: #6c5053;\n"
"}")

        self.verticalLayout.addWidget(self.button_language)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jalali Date(\u062a\u0627\u0631\u06cc\u062e \u062c\u0644\u0627\u0644\u06cc)", None))
        self.label_date_value.setText(QCoreApplication.translate("MainWindow", u"1401-11-19", None))
        self.label_date.setStyleSheet("")
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e \u0627\u0645\u0631\u0648\u0632 :", None))
        self.label_year_value.setText(QCoreApplication.translate("MainWindow", u"1401", None))
        self.label_year.setStyleSheet("")
        self.label_year.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u0644 :", None))
        self.label_month_value.setText(QCoreApplication.translate("MainWindow", u"bahman", None))
        self.label_month.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0627\u0647 :", None))
        self.label_day_value.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_day.setStyleSheet("")
        self.label_day.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0648\u0632 :", None))
        self.label_time_value.setText(QCoreApplication.translate("MainWindow", u"01:11:45", None))
        self.label_time.setStyleSheet("")
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0627\u0639\u062a :", None))
        self.button_language.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0627\u0631\u0633\u06cc", None))
    # retranslateUi

