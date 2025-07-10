from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class StatisticsPage(QDialog):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("Statistics")
        self.resize(1000, 700)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # DB-დან მონაცემების აღება
        patients = self.db.fetch_patients()

        # Chart პიროვნების ტიპებზე
        counts = {"Introvert": 0, "Extrovert": 0}
        for patient in patients:
            personality = patient[-1]
            if personality in counts:
                counts[personality] += 1

        pie_series = QPieSeries()
        for key, value in counts.items():
            pie_series.append(key, value)

        pie_chart = QChart()
        pie_chart.addSeries(pie_series)
        pie_chart.setTitle("Personality Distribution")

        pie_chart_view = QChartView(pie_chart)
        pie_chart_view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(QLabel("Personality Distribution Pie Chart"))
        layout.addWidget(pie_chart_view)

#chart სვეტოვანი დიაგრამა ასაკზე
        age_counts = {}
        for p in patients:
            age = p[3]
            if age is not None:
                age_counts[age] = age_counts.get(age, 0) + 1

        sorted_ages = sorted(age_counts.keys())
        counts = [age_counts[age] for age in sorted_ages]

        bar_set = QBarSet("Age Count")
        bar_set.append(counts)

        bar_series = QBarSeries()
        bar_series.append(bar_set)

        bar_chart = QChart()
        bar_chart.addSeries(bar_series)
        bar_chart.setTitle("Age Distribution")

        categories = [str(age) for age in sorted_ages]
        axisX = QBarCategoryAxis()
        axisX.append(categories)

        bar_chart.createDefaultAxes()
        bar_chart.setAxisX(axisX, bar_series)

        bar_chart.legend().setVisible(True)
        bar_chart.legend().setAlignment(Qt.AlignBottom)

        bar_chart_view = QChartView(bar_chart)
        bar_chart_view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(QLabel("Age Distribution Bar Chart"))
        layout.addWidget(bar_chart_view)
