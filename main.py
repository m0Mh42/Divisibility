from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt
import sys
# m0Mh42

class DivisibilityUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self._centeralwidget = QWidget()
        self.setCentralWidget(self._centeralwidget)
        self.vboxlayout = QVBoxLayout()
        self._centeralwidget.setLayout(self.vboxlayout)
        self._statusbar = self.statusBar()
        self._statusbar.showMessage("Ready")
        # self.setStatusTip("Ready")
        self._createUI()
        self.setFixedSize(500, 250)
        self.setWindowTitle("Divisibility")

    def _createUI(self):
        self.numberentry = QLineEdit()
        self.numberentry.setFixedSize(80, 20)
        self.startbutton = QPushButton("Start")
        self.startbutton.setFixedSize(80, 25)
        self.startbutton.setStatusTip("Start")
        self.showtext = QTextEdit()
        self.showtext.setReadOnly(True)
        self.vboxlayout.addWidget(self.numberentry, Qt.AlignTop)
        self.vboxlayout.addWidget(self.startbutton)
        self.vboxlayout.addWidget(self.showtext, Qt.AlignTop)

    def addNumberToLabel(self, number: int):
        print ("Adding " + str(number))
        _number = str(number)
        _text = self.showtext.toPlainText()
        self.showtext.setText(_text + ', ' + _number)

    def clearLabelText(self):
        print("Text Clear")
        self.showtext.setText('1')

class DivisibilityCtrl:
    def __init__(self, model, ui: DivisibilityUI):
        self._ui = ui
        self._model = model
        self._connectControls()

    def _connectControls(self):
        self._ui.startbutton.clicked.connect(self.startProcess)
        self._ui.numberentry.returnPressed.connect(self.startProcess)

    def startProcess(self):
        text = self._ui.numberentry.text()
        if text == "":
            self._ui.showtext.setText("Please enter a number")
            return
        try:
            number = eval(text)
            model = DivisibilityModel(self._ui)
            model.process(number=number)
            self._ui._statusbar.showMessage("Done")
        except:
            self._ui.showtext.setText("Please enter a valid number")

class DivisibilityModel:
    def __init__(self, ui: DivisibilityUI):
        self._ui = ui

    def process(self, number):
        self._ui._statusbar.showMessage("Working")
        self._ui.clearLabelText()
        for i in range(2, number):
            if (number % i) == 0:
                print ("Attempting to add " + str(i))
                self._ui.addNumberToLabel(number=i)
        self._ui.addNumberToLabel(number)

def main():
    app = QApplication(sys.argv)
    view = DivisibilityUI()
    view.show()
    model = DivisibilityModel(view)
    ctrl = DivisibilityCtrl(model=model, ui=view)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
