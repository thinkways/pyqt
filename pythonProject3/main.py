from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QDate, QDateTime, QTime
import sys
from untitled import Ui_Form


class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lineEdit.setInputMask("99:99")

    def on_pushButton_readTime_clicked(self):
        curTime = QDateTime.currentDateTime()
        self.ui.timeEdit.setTime(curTime.time())
        self.ui.lineEdit.setText(curTime.toString("hh:mm"))
        self.ui.dateTimeEdit.setDateTime(curTime)
        self.ui.lineEdit_3.setText(curTime.toString("yyyy年MM月dd日 hh:mm:z"))
        self.ui.dateEdit.setDate(curTime.date())
        self.ui.lineEdit_2.setText(curTime.toString("yyyy/MM/dd"))

    def on_pushButton_clicked(self):
        tmstr = self.ui.lineEdit.text()
        tm = QTime.fromString(tmstr, "hh:mm")
        self.ui.timeEdit.setTime(tm)

    def on_pushButton_2_clicked(self):
        dateStr = self.ui.lineEdit_2.text()
        date = QDate.fromString(dateStr, "yyyyMMdd")
        self.ui.dateEdit.setDate(date)

    def on_pushButton_3_clicked(self):
        dttmStr = self.ui.lineEdit_3.text()
        dttm = QDateTime.fromString(dttmStr, "yyyyMMdd hhmm")
        self.ui.dateTimeEdit.setDateTime(dttm)

    def on_calendarWidget_selectionChanged(self):
        dt = self.ui.calendarWidget.selectedDate()
        self.ui.lineEdit_4.setText(dt.toString("yyyy/MM/dd"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demoApp = MyApp()
    demoApp.show()
    sys.exit(app.exec_())
