from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout, QLineEdit
)

from Literals import Literal

class Gui_sensors(QWidget):
    def __init__(self, config, num):
        super().__init__()

        self.num = num
        self.id_current = 0
        self.type_current = 0
        self.var_current = 0

        self.type_sensors_value = list(Literal.sensor_type_single_gui.keys())
        self.type_sensors_name = list(Literal.sensor_type_single_gui.values())

        self.config = config
        self.var_sensors = list(config.Ai.keys())

        self.prev_i = 0

        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()

        self.name_sensor = QLabel(f"Сенсор №{self.num}")
        self.main_layout.addWidget(self.name_sensor)

        self.layout_id = QHBoxLayout()
        self.id_name = QLabel("ID:")
        self.id_edit = QLineEdit('0')
        self.layout_id.addWidget(self.id_name)
        self.layout_id.addWidget(self.id_edit)
        self.main_layout.addLayout(self.layout_id)

        self.layout_type = QHBoxLayout()
        self.type_name = QLabel("Тип:")
        self.type_combo = QComboBox()
        self.type_combo.addItems(self.type_sensors_name)
        self.layout_type.addWidget(self.type_name)
        self.layout_type.addWidget(self.type_combo)
        self.main_layout.addLayout(self.layout_type)

        self.layout_var = QHBoxLayout()
        self.var_name = QLabel("Var:")
        self.var_combo = QComboBox()
        self.var_combo.addItems(self.var_sensors)
        self.layout_var.addWidget(self.var_name)
        self.layout_var.addWidget(self.var_combo)
        self.main_layout.addLayout(self.layout_var)

        self.setLayout(self.main_layout)

        pass

    def clear(self):
        self.id_edit.setText(str(0))
        self.type_combo.setCurrentIndex(0)
        self.var_combo.setCurrentIndex(0)
