from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout, QLineEdit
)

from Literals import Literal

class Gui_humidifier(QWidget):
    def __init__(self):
        super().__init__()

        self.hum_use = False

        self.initUI()

    def initUI(self):
        self.main_layout = QHBoxLayout()

        self.layout_hum = QVBoxLayout()

        self.hum_name = QLabel("Увлажнитель:")
        self.layout_hum.addWidget(self.hum_name)

        self.hum_use_layout = QHBoxLayout()
        self.hum_use_label = QLabel("Используется:")
        self.hum_use_combo = QComboBox()
        self.hum_use_combo.addItems(['Нет', 'Используется'])

        self.hum_use_layout.addWidget(self.hum_use_label)
        self.hum_use_layout.addWidget(self.hum_use_combo)

        self.layout_hum.addLayout(self.hum_use_layout)

        self.drainag_name = QLabel("Осушение:")
        self.layout_hum.addWidget(self.drainag_name)

        self.drainage_use_layout = QHBoxLayout()
        self.drainage_use_label = QLabel("Используется:")
        self.drainage_use_combo = QComboBox()
        self.drainage_use_combo.addItems(['Нет', 'Используется'])

        self.drainage_use_layout.addWidget(self.drainage_use_label)
        self.drainage_use_layout.addWidget(self.drainage_use_combo)

        self.layout_hum.addLayout(self.drainage_use_layout)

        self.main_layout.addLayout(self.layout_hum)

        self.setLayout(self.main_layout)
