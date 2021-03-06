from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer
import sys
from untitled import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer(self)
        self.timer.stop()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time_info)
        self.ui.pushBtn_set.clicked.connect(self.do_setInterval)
        self.sec = 0
        self.min = 0
        self.hour = 0

    def on_pushBtn_start_clicked(self):
        self.sec, self.min, self.hour = 0, 0, 0
        self.do_setInterval()
        self.ui.pushBtn_start.setEnabled(False)
        self.ui.pushBtn_stop.setEnabled(True)

    def on_pushBtn_stop_clicked(self):
        self.timer.stop()
        self.ui.pushBtn_stop.setEnabled(False)
        self.ui.pushBtn_start.setEnabled(True)

    def do_setInterval(self):
        self.timer.stop()
        self.timer.setInterval(int(self.ui.lineEdit.text()))
        self.timer.start()

    def update_time_info(self):
        self.sec = self.sec + self.timer.interval() / 1000
        self.min = self.min + int(self.sec) // 60
        self.hour = self.hour + self.min // 60
        if self.min:
            self.sec = self.sec % 60
        if self.hour:
            self.min = self.min % 60
        self.hour = self.hour % 24

        self.ui.lcdNumber_sec.display(str(int(self.sec)))
        self.ui.lcdNumber_min.display(str(self.min))
        self.ui.lcdNumber_hour.display(str(self.hour))
        self.statusBar().showMessage("hello")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoApp = MyApp()
    demoApp.show()
    sys.exit(app.exec_())











