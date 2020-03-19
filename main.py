import sys

from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem
from design import Ui_Form


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.adder)

    def adder(self):
        if self.lineEdit.text() == '' or self.lineEdit_2.text() == '':
            self.label_3.setText('Error')
        else:
            text = [self.lineEdit.text(), self.lineEdit_2.text()]
            self.listWidget.addItem(QListWidgetItem('\t'.join(text)))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
