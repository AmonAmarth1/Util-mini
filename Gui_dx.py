from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout, QLineEdit
)

from Literals import Literal

class Gui_dx(QWidget):
    def __init__(self):
        super().__init__()

        self.dx_use = False
        self.dx_type = 0

        self.type_dx_num = list(Literal.type_dx_num.keys())
        self.type_dx_name = list(Literal.type_dx_num.values())

        self.initUI()

    def initUI(self):
        self.main_layout = QHBoxLayout()

        self.layout_dx = QVBoxLayout()

        self.dx_name = QLabel("Охладитель:")
        self.layout_dx.addWidget(self.dx_name)

        self.dx_use_layout = QHBoxLayout()
        self.dx_use_label = QLabel("Используется:")
        self.dx_use_combo = QComboBox()
        self.dx_use_combo.addItems(['Нет', 'Используется'])
        self.dx_use_layout.addWidget(self.dx_use_label)
        self.dx_use_layout.addWidget(self.dx_use_combo)
        self.layout_dx.addLayout(self.dx_use_layout)

        self.layout_dx_type = QHBoxLayout()
        self.type_dx_label = QLabel("Тип:")
        self.type_dx_combo = QComboBox()
        self.type_dx_combo.addItems(self.type_dx_name)
        self.layout_dx_type.addWidget(self.type_dx_label)
        self.layout_dx_type.addWidget(self.type_dx_combo)
        self.layout_dx.addLayout(self.layout_dx_type)

        self.dx_heat_layout = QHBoxLayout()
        self.dx_heat_label = QLabel("Нагрев Dx:")
        self.dx_heat_combo = QComboBox()
        self.dx_heat_combo.addItems(['Нет', 'Используется'])
        self.dx_heat_layout.addWidget(self.dx_heat_label)
        self.dx_heat_layout.addWidget(self.dx_heat_combo)
        self.layout_dx.addLayout(self.dx_heat_layout)

        self.main_layout.addLayout(self.layout_dx)

        self.setLayout(self.main_layout)
