from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout, QLineEdit
)

from Literals import Literal

class Gui_Recup(QWidget):
    def __init__(self):
        super().__init__()

        self.recup_use = False
        self.recup_type = 0

        self.heat2_use = False

        self.heat1_reserve_pump_use = False
        self.heat2_reserve_pump_use = False

        self.type_recup_num = list(Literal.type_recup_num.keys())
        self.type_recup_name = list(Literal.type_recup_num.values())

        self.type_conv = list(Literal.types_converter.keys())

        self.initUI()

    def initUI(self):
        self.main_layout = QHBoxLayout()

        self.layout_recup = QVBoxLayout()

        self.recup_name = QLabel("Рекуператор")
        self.layout_recup.addWidget(self.recup_name)

        self.recup_use_layout = QHBoxLayout()
        self.recup_use_label = QLabel("Используется")
        self.recup_use_combo = QComboBox()
        self.recup_use_combo.addItems(['Нет', 'Используется'])
        self.recup_use_layout.addWidget(self.recup_use_label)
        self.recup_use_layout.addWidget(self.recup_use_combo)
        self.layout_recup.addLayout(self.recup_use_layout)

        self.layout_recup_type = QHBoxLayout()
        self.recup_type_label = QLabel("Тип:")
        self.recup_type_combo = QComboBox()
        self.recup_type_combo.addItems(self.type_recup_name)
        self.recup_type_combo.currentIndexChanged.connect(self.showModbus)
        self.layout_recup_type.addWidget(self.recup_type_label)
        self.layout_recup_type.addWidget(self.recup_type_combo)
        self.layout_recup.addLayout(self.layout_recup_type)

        self.recup_modbus_use_layout = QHBoxLayout()
        self.recup_modbus_use_label = QLabel("Modbus:")
        self.recup_modbus_use_combo = QComboBox()
        self.recup_modbus_use_combo.addItems(['Нет', 'Используется'])
        self.recup_modbus_use_combo.currentIndexChanged.connect(self.showRotorParam)
        self.recup_modbus_use_layout.addWidget(self.recup_modbus_use_label)
        self.recup_modbus_use_layout.addWidget(self.recup_modbus_use_combo)
        self.layout_recup.addLayout(self.recup_modbus_use_layout)

        self.recup_modbus_use_label.hide()
        self.recup_modbus_use_combo.hide()

        self.layout_recup_id = QHBoxLayout()
        self.recup_id_label = QLabel("Id:")
        self.recup_id_edit = QLineEdit(str(40))
        self.layout_recup_id.addWidget(self.recup_id_label)
        self.layout_recup_id.addWidget(self.recup_id_edit)
        self.layout_recup.addLayout(self.layout_recup_id)

        self.recup_id_label.hide()
        self.recup_id_edit.hide()

        self.layout_recup_rpm = QHBoxLayout()
        self.recup_rpm_label = QLabel("Номинальные обороты:")
        self.recup_rpm_edit = QLineEdit(str(10))
        self.layout_recup_rpm.addWidget(self.recup_rpm_label)
        self.layout_recup_rpm.addWidget(self.recup_rpm_edit)
        self.layout_recup.addLayout(self.layout_recup_rpm)

        self.recup_rpm_label.hide()
        self.recup_rpm_edit.hide()

        self.recup_conv_type_layout = QHBoxLayout()
        self.recup_name_conv_label = QLabel("Тип ПЧ")
        self.recup_conv_type_combo = QComboBox()
        self.recup_conv_type_combo.addItems(self.type_conv)
        self.recup_conv_type_layout.addWidget(self.recup_name_conv_label)
        self.recup_conv_type_layout.addWidget(self.recup_conv_type_combo)
        self.layout_recup.addLayout(self.recup_conv_type_layout)

        self.recup_name_conv_label.hide()
        self.recup_conv_type_combo.hide()

        self.main_layout.addLayout(self.layout_recup)

        self.setLayout(self.main_layout)

        pass

    def showModbus(self):
        if self.recup_type_combo.currentIndex() == 2:
            self.recup_modbus_use_label.show()
            self.recup_modbus_use_combo.show()
        else:
            self.recup_modbus_use_label.hide()
            self.recup_modbus_use_combo.hide()

    def showRotorParam(self):
        if self.recup_modbus_use_combo.currentIndex() == 1:
            self.recup_id_label.show()
            self.recup_id_edit.show()
            self.recup_rpm_label.show()
            self.recup_rpm_edit.show()
            self.recup_name_conv_label.show()
            self.recup_conv_type_combo.show()
        else:
            self.recup_id_label.hide()
            self.recup_id_edit.hide()
            self.recup_rpm_label.hide()
            self.recup_rpm_edit.hide()
            self.recup_name_conv_label.hide()
            self.recup_conv_type_combo.hide()
