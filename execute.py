import sys
from time import sleep

from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc

from ui_main_window import Ui_MainWindow
from jalali_date_time import JalaliDateTime
import resources


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # add window icon (using resources.py)
        self.setWindowIcon(qtg.QIcon(":/date_time_icon"))

        # create jalali date time object
        self.jdt = JalaliDateTime()

        # import .ui file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # call button language method manually for the first time just to set label values
        self.button_language_clicked()

        # set font for widgets, and make labels selectable
        for i in self.children():
            if type(i) == qtw.QLabel:
                i.setFont(qtg.QFont("Times New Roman", 30))
                i.setTextInteractionFlags(qtc.Qt.TextInteractionFlag.TextSelectableByMouse)

        # set font for button language
        self.ui.button_language.setFont(qtg.QFont("Times New Roman", 30))

        # create a timer to update time every second
        self.timer = qtc.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.label_time_value_updated)
        self.timer.start()

        # connect button to the method
        self.ui.button_language.clicked.connect(self.button_language_clicked)

        self.show()

    def label_time_value_updated(self):
        if self.ui.button_language.text() == 'english':
            self.ui.label_time_value.setText(self.jdt.time_fa)
        else:
            self.ui.label_time_value.setText(self.jdt.time_en)

        if self.jdt.hour_en == '23' and self.jdt.minute_en == '59' and self.jdt.second_en == '59':
            sleep(2)
            self.button_language_clicked()
            self.button_language_clicked()

    def button_language_clicked(self):
        if self.ui.button_language.text() == 'english':

            self.ui.label_date.setText('Today :')
            self.ui.label_date_value.setText(self.jdt.date_en)
            self.ui.grid_layout_date.addWidget(self.ui.label_date, 0, 0)
            self.ui.grid_layout_date.addWidget(self.ui.label_date_value, 0, 1)

            self.ui.label_year.setText('Year :')
            self.ui.label_year_value.setText(self.jdt.year_en)
            self.ui.grid_layout_year.addWidget(self.ui.label_year, 0, 0)
            self.ui.grid_layout_year.addWidget(self.ui.label_year_value, 0, 1)

            self.ui.label_month.setText('Month :')
            self.ui.label_month_value.setText(self.jdt.month_name_en)
            self.ui.grid_layout_month.addWidget(self.ui.label_month, 0, 0)
            self.ui.grid_layout_month.addWidget(self.ui.label_month_value, 0, 1)

            self.ui.label_day.setText('Day :')
            self.ui.label_day_value.setText(self.jdt.day_en)
            self.ui.grid_layout_day.addWidget(self.ui.label_day, 0, 0)
            self.ui.grid_layout_day.addWidget(self.ui.label_day_value, 0, 1)

            self.ui.label_time.setText('Time :')
            self.ui.label_time_value.setText(self.jdt.time_en)
            self.ui.grid_layout_time.addWidget(self.ui.label_time, 0, 0)
            self.ui.grid_layout_time.addWidget(self.ui.label_time_value, 0, 1)

            self.ui.button_language.setText('فارسی')

        else:

            self.ui.label_date.setText('تاریخ امروز :')
            self.ui.label_date_value.setText(self.jdt.date_fa)
            self.ui.grid_layout_date.addWidget(self.ui.label_date, 0, 1)
            self.ui.grid_layout_date.addWidget(self.ui.label_date_value, 0, 0)

            self.ui.label_year.setText('سال :')
            self.ui.label_year_value.setText(self.jdt.year_fa)
            self.ui.grid_layout_year.addWidget(self.ui.label_year, 0, 1)
            self.ui.grid_layout_year.addWidget(self.ui.label_year_value, 0, 0)

            self.ui.label_month.setText('ماه :')
            self.ui.label_month_value.setText(self.jdt.month_name_fa)
            self.ui.grid_layout_month.addWidget(self.ui.label_month, 0, 1)
            self.ui.grid_layout_month.addWidget(self.ui.label_month_value, 0, 0)

            self.ui.label_day.setText('روز :')
            self.ui.label_day_value.setText(self.jdt.day_fa)
            self.ui.grid_layout_day.addWidget(self.ui.label_day, 0, 1)
            self.ui.grid_layout_day.addWidget(self.ui.label_day_value, 0, 0)

            self.ui.label_time.setText('ساعت :')
            self.ui.label_time_value.setText(self.jdt.time_fa)
            self.ui.grid_layout_time.addWidget(self.ui.label_time, 0, 1)
            self.ui.grid_layout_time.addWidget(self.ui.label_time_value, 0, 0)

            self.ui.button_language.setText('english')


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
