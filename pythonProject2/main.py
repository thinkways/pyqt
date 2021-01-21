from PyQt5.QtWidgets import QWidget, QApplication
from untitled import Ui_Form
from PyQt5.QtCore import pyqtSlot
import sys


class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    @pyqtSlot(int)
    def on_horizontalSlider_valueChanged(self, value):
        self.ui.progressBar.setValue(value)

    def on_horizontalScrollBar_valueChanged(self, value):
        self.ui.progressBar.setValue(value)

    @pyqtSlot(bool)
    def on_checkBox_txtVis_clicked(self, checked):
        self.ui.progressBar.setTextVisible(checked)

    @pyqtSlot(bool)
    def on_checkBox_invert_clicked(self, checked):
        self.ui.progressBar.setInvertedAppearance(checked)

    def on_radioBtn_percnet_clicked(self):
        self.ui.progressBar.setFormat("%p%")

    def on_radioBtn_value_clicked(self):
        self.ui.progressBar.setFormat("%v")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoApp = MyApp()
    demoApp.show()
    sys.exit(app.exec_())