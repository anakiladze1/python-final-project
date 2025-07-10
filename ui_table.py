from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QAbstractItemView
from PyQt5 import QtCore
from window2 import Ui_Dialog

class TablePage(QDialog):
    def __init__(self, db, switch_to_add, switch_to_statistics):
        super().__init__()
        self.db = db
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

        self.ui.pushButton.clicked.connect(switch_to_add)           # Add
        self.ui.pushButton_2.clicked.connect(switch_to_statistics)  # Statistic
        self.ui.pushButton_3.clicked.connect(self.delete_patient)   # Delete
        self.ui.pushButton_4.clicked.connect(self.update_patient)   # Update

        self.load_data()

    def load_data(self):
        self.ui.tableWidget.setRowCount(0)
        patients = self.db.fetch_patients()

        self.ui.tableWidget.setColumnCount(9)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            "Patient ID", "Name and Surname", "Gender", "Age", "Time Alone",
            "Events", "Drained", "Friends", "Personality"
        ])

        for row_data in patients:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            for col, item in enumerate(row_data):
                cell = QTableWidgetItem(str(item))
                cell.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row, col, cell)

    def delete_patient(self):
        row = self.ui.tableWidget.currentRow()
        if row < 0:
            QMessageBox.warning(self, "No Selection", "Please select a row to delete.")
            return

        patient_id = int(self.ui.tableWidget.item(row, 0).text())
        self.db.delete_patient(patient_id)
        self.load_data()
        QMessageBox.information(self, "Success", "Patient was successfully deleted.")

    def update_patient(self):
        row = self.ui.tableWidget.currentRow()
        if row < 0:
            QMessageBox.warning(self, "No Selection", "Please select a row to update.")
            return

        patient_id = int(self.ui.tableWidget.item(row, 0).text())
        age = int(self.ui.tableWidget.item(row, 3).text())
        time_alone = int(self.ui.tableWidget.item(row, 4).text())
        events = int(self.ui.tableWidget.item(row, 5).text())
        drained = self.ui.tableWidget.item(row, 6).text()
        friends = int(self.ui.tableWidget.item(row, 7).text())
        personality = self.ui.tableWidget.item(row, 8).text()

        self.db.update_patient(patient_id, age, time_alone, events, drained, friends, personality)
        self.load_data()
        QMessageBox.information(self, "Updated", "Patient data was updated successfully.")
