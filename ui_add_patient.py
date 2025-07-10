from PyQt5.QtWidgets import QDialog, QMessageBox
from window3 import Ui_Dialog

class AddPatientPage(QDialog):
    def __init__(self, db, back_to_table):
        super().__init__()
        self.db = db
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.back_to_table = back_to_table
        self.ui.pushButton.clicked.connect(back_to_table)
        self.ui.pushButton_2.clicked.connect(self.save_patient)

    def save_patient(self):
        name = self.ui.lineEdit_2.text()
        age = int(self.ui.lineEdit.text())
        gender = "Male" if self.ui.radioButton_2.isChecked() else "Female"
        alone = int(self.ui.lineEdit_3.text())
        events = int(self.ui.lineEdit_4.text())
        drained = "Yes" if self.ui.checkBox.isChecked() else "No"
        friends = int(self.ui.lineEdit_5.text())

        personality = "Introvert" if friends < 10 and drained == "Yes" and events < 10 else "Extrovert"

        self.db.insert_patient(name, gender, age,
                               alone, events,
                               drained, friends, personality)

        QMessageBox.information(self, "Success", f"Classified as: {personality}")
        self.back_to_table()
