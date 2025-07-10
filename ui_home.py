from PyQt5.QtWidgets import QDialog
from window1 import Ui_Dialog

class HomePage(QDialog):
    def __init__(self, switch_to_table):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(switch_to_table)