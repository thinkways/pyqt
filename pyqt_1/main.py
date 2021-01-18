from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5.QtGui import QFont
import sys
from untitled import Ui_MainWindow


class Myapp(QMainWindow):
    def __init__(self):
        super(Myapp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.spinBox_quantity.valueChanged.connect(self.setSpinboxValue)
        self.ui.spinBox_price.valueChanged.connect(self.setSpinboxValue)

    def on_pushButton_clicked(self):
        quantity = int(self.ui.lineEdit_quantity.text())
        price = float(self.ui.lineEdit_price.text())
        self.ui.lineEdit_sum.setText('{:.6f}'.format(quantity * price))

    def setSpinboxValue(self):
        quantity = self.ui.spinBox_quantity.value()
        price = self.ui.spinBox_price.value()
        self.ui.spinBox_sum.setValue(quantity * price)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demoapp = Myapp()
    demoapp.show()
    sys.exit(app.exec_())

