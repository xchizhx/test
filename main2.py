import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLineEdit


class WidgetsHideNSeek(QWidget):
    def __init__(self):
        super().__init__()
        self.checkbox4 = None
        self.checkbox3 = None
        self.checkbox2 = None
        self.checkbox1 = None
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 700, 300)
        self.setWindowTitle('Вторая программа')

        self.checkbox1 = QCheckBox('edit1', self)
        self.checkbox1.resize(200, 20)
        self.checkbox1.move(10, 100)
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(self.click)

        self.checkbox2 = QCheckBox('edit2', self)
        self.checkbox2.resize(200, 20)
        self.checkbox2.move(10, 125)
        self.checkbox2.setChecked(True)
        self.checkbox2.stateChanged.connect(self.click)

        self.checkbox3 = QCheckBox('edit3', self)
        self.checkbox3.resize(200, 20)
        self.checkbox3.move(10, 150)
        self.checkbox3.setChecked(True)
        self.checkbox3.stateChanged.connect(self.click)

        self.checkbox4 = QCheckBox('edit4', self)
        self.checkbox4.resize(200, 20)
        self.checkbox4.move(10, 175)
        self.checkbox4.setChecked(True)
        self.checkbox4.stateChanged.connect(self.click)

        self.edit1 = QLineEdit('Поле edit1', self)
        self.edit1.resize(100, 20)
        self.edit1.move(100, 100)

        self.edit2 = QLineEdit('Поле edit2', self)
        self.edit2.resize(100, 20)
        self.edit2.move(100, 125)

        self.edit3 = QLineEdit('Поле edit3', self)
        self.edit3.resize(100, 20)
        self.edit3.move(100, 150)

        self.edit4 = QLineEdit('Поле edit4', self)
        self.edit4.resize(100, 20)
        self.edit4.move(100, 175)

    def click(self):
        objDict = {'edit1': self.edit1,
                   'edit2': self.edit2,
                   'edit3': self.edit3,
                   'edit4': self.edit4}
        if self.sender().isChecked():
            objDict[self.sender().text()].show()
        else:
            objDict[self.sender().text()].hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetsHideNSeek()
    ex.show()
    sys.exit(app.exec())
