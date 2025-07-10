import sys
from PyQt5.QtWidgets import QApplication
from database import Database
from MainWindow import MainWindow

app = QApplication(sys.argv)
db = Database()
window = MainWindow(db)
window.show()
sys.exit(app.exec_())
