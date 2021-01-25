from PyQt5.QtWidgets import QWidget, QApplication
import sys
from untitled import Ui_Form


class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoApp = MyApp()
    demoApp.show()
    sys.exit(app.exec_())
