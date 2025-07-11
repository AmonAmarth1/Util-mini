from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout, QLineEdit
)

from Literals import Literal

class Gui_Heat(QWidget):
    def __init__(self):
        super().__init__()

        self.heat1_type = False
        self.heat2_type = False

        self.heat2_use = False

        self.heat1_reserve_pump_use = False
        self.heat2_reserve_pump_use = False


        self.type_heat_num = list(Literal.type_heat_num.keys())
        self.type_heat_name = list(Literal.type_heat_num.values())
        self.type_heat_pump_reserve_num = list(Literal.type_heat_pump_reserve.keys())
        self.type_heat_pump_reserve_name = list(Literal.type_heat_pump_reserve.values())

        self.initUI()

    def initUI(self):
        self.main_layout = QHBoxLayout()

        self.layout_heat1 = QVBoxLayout()
        self.layout_heat2 = QVBoxLayout()

        self.heat1_name = QLabel("Нагреватель 1:")
        self.layout_heat1.addWidget(self.heat1_name)

        self.layout_heat1_type = QHBoxLayout()
        self.heat1_type_label = QLabel("Тип:")
        self.heat1_type_combo = QComboBox()
        self.heat1_type_combo.addItems(self.type_heat_name)
        self.layout_heat1_type.addWidget(self.heat1_type_label)
        self.layout_heat1_type.addWidget(self.heat1_type_combo)
        self.layout_heat1.addLayout(self.layout_heat1_type)

        self.layout_heat1_reserve_pump = QHBoxLayout()
        self.heat1_reserve_pump_label = QLabel("Резервный насос:")
        self.heat1_reserve_pump_combo = QComboBox()
        self.heat1_reserve_pump_combo.addItems(self.type_heat_pump_reserve_name)
        self.layout_heat1_reserve_pump.addWidget(self.heat1_reserve_pump_label)
        self.layout_heat1_reserve_pump.addWidget(self.heat1_reserve_pump_combo)
        self.layout_heat1.addLayout(self.layout_heat1_reserve_pump)

        self.main_layout.addLayout(self.layout_heat1)

        self.heat2_name = QLabel("Нагреватель 2:")
        self.layout_heat2.addWidget(self.heat2_name)

        self.heat2_use = QHBoxLayout()
        self.heat2_use_label = QLabel("Используется:")
        self.heat2_use_combo = QComboBox()
        self.heat2_use_combo.addItems(['Нет', 'Используется'])
        self.heat2_use.addWidget(self.heat2_use_label)
        self.heat2_use.addWidget(self.heat2_use_combo)
        self.layout_heat2.addLayout(self.heat2_use)

        self.heat2_type_layout = QHBoxLayout()
        self.heat2_type_label = QLabel("Тип:")
        self.heat2_type_combo = QComboBox()
        self.heat2_type_combo.addItems(self.type_heat_name)
        self.heat2_type_layout.addWidget(self.heat2_type_label)
        self.heat2_type_layout.addWidget(self.heat2_type_combo)
        self.layout_heat2.addLayout(self.heat2_type_layout)

        self.layout_heat2_reserve_pump = QHBoxLayout()
        self.heat2_reserve_pump_label = QLabel("Резервный насос:")
        self.heat2_reserve_pump_combo = QComboBox()
        self.heat2_reserve_pump_combo.addItems(self.type_heat_pump_reserve_name)
        self.layout_heat2_reserve_pump.addWidget(self.heat2_reserve_pump_label)
        self.layout_heat2_reserve_pump.addWidget(self.heat2_reserve_pump_combo)
        self.layout_heat2.addLayout(self.layout_heat2_reserve_pump)


        self.main_layout.addLayout(self.layout_heat2)

        self.setLayout(self.main_layout)

        pass

    def clear(self):
        self.heat1_type_combo.setCurrentIndex(0)
        self.heat1_reserve_pump_combo.setCurrentIndex(0)
        self.heat2_use_combo.setCurrentIndex(0)
        self.heat2_type_combo.setCurrentIndex(0)
        self.heat2_reserve_pump_combo.setCurrentIndex(0)

