
from PyQt5.QtWidgets import QStackedWidget
from ui_home import HomePage
from ui_table import TablePage
from ui_add_patient import AddPatientPage
from StatisticsPage import StatisticsPage

class MainWindow(QStackedWidget):
    def __init__(self, db):
        super().__init__()

        self.db = db

        self.home_page = HomePage(self.go_to_table_page)
        self.table_page = TablePage(self.db, self.go_to_add_page, self.open_statistics)
        self.add_page = AddPatientPage(self.db, self.go_to_table_page)

        self.addWidget(self.home_page)   # index 0
        self.addWidget(self.table_page)  # index 1
        self.addWidget(self.add_page)    # index 2

        self.setFixedSize(1600, 863)
        self.setWindowTitle("Psychologist's Portal")
        self.setCurrentIndex(0)

    def go_to_table_page(self):
        self.table_page.load_data()
        self.setCurrentIndex(1)

    def go_to_add_page(self):
        self.setCurrentIndex(2)

    def open_statistics(self):
        dialog = StatisticsPage(self.db)
        dialog.exec_()
