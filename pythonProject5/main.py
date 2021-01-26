import sys
from PyQt5.QtWidgets import QWidget, QApplication
from untitled import Ui_Form


class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushBtn_initSimple.clicked.connect(self.do_initSimple)
        self.ui.pushBtn_clear.clicked.connect(self.ui.comboBox.clear)
        self.ui.checkBox_editable.toggled.connect(self.ui.comboBox.setEditable)
        self.ui.comboBox.currentIndexChanged[str].connect(self.ui.lineEdit.setText)
        self.ui.pushBtn_initCplex.clicked.connect(self.do_initComplex)

    def do_initSimple(self):
        info = ["bob", "sean", "ketty"]
        self.ui.comboBox.clear()
        for item in info:
            self.ui.comboBox.addItem(item)

    def do_initComplex(self):
        info = {"bob": 22, "sean": 34, "ketty": 18}
        self.ui.comboBox_withUserData.clear()
        for key, value in info.items():
            self.ui.comboBox_withUserData.addItem(key, value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoApp = MyApp()
    demoApp.show()
    sys.exit(app.exec_())
