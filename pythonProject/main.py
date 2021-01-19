import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from untitled import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushBtn_bold.clicked[bool].connect(self.fontStyle)
        self.ui.pushBtn_italic.clicked[bool].connect(self.fontStyle)
        self.ui.pushBtn_underline.clicked[bool].connect(self.fontStyle)

    def on_pushBtn_alignleft_clicked(self):
        self.ui.textEdit.setAlignment(Qt.AlignLeft)

    def on_pushBtn_aligncenter_clicked(self):
        self.ui.textEdit.setAlignment(Qt.AlignCenter)

    def on_pushBtn_alignright_clicked(self):
        self.ui.textEdit.setAlignment(Qt.AlignRight)

    @pyqtSlot(bool)
    def on_checkBox_readonly_clicked(self, clicked):
        self.ui.textEdit.setReadOnly(clicked)

    @pyqtSlot(bool)
    def on_checkBox_checkBox_enabled_clicked(self, clicked):
        self.ui.textEdit.setEnabled(clicked)

    def fontStyle(self, flag):
        font = self.ui.textEdit.font()

        if self.sender() is self.ui.pushBtn_bold:
            font.setBold(flag)
        if self.sender() is self.ui.pushBtn_italic:
            font.setItalic(flag)
        if self.sender() is self.ui.pushBtn_underline:
            font.setUnderline(flag)

        self.ui.textEdit.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoApp = MyApp()
    demoApp.show()
    sys.exit(app.exec_())
