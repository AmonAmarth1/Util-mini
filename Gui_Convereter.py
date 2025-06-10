from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout, QLineEdit
)

from Literals import Literal

class Gui_Converter(QWidget):
    def __init__(self):
        super().__init__()

        self.in_num = 0
        self.out_num = 0

        self.in_type = 2
        self.out_type = 2

        self.out_use = False

        self.in_modbus_use = False
        self.out_modbus_use = False

        self.in_reserve = 0
        self.out_reserve = 0

        self.in_main_group = 0
        self.in_reserve_group = 0

        self.out_main_group = 0
        self.out_reserve_group = 0

        self.type_conv = list(Literal.types_converter.keys())
        self.reserve = list(Literal.reserve_converter.values())

        self.initUI()

    def initUI(self):
        self.main_layout = QHBoxLayout()

        self.layout_in = QVBoxLayout()
        self.layout_out = QVBoxLayout()

        self.name_in = QLabel("Вентилятор приток")
        self.layout_in.addWidget(self.name_in)

        self.layout_in_num = QHBoxLayout()
        self.name_in_num = QLabel("Количество")
        self.in_num_edit = QLineEdit('1')
        self.layout_in_num.addWidget(self.name_in_num)
        self.layout_in_num.addWidget(self.in_num_edit)
        self.layout_in.addLayout(self.layout_in_num)

        self.layout_in_modbus_use = QHBoxLayout()
        self.name_in_modbus_use = QLabel("Тип управления")
        self.combo_in_modbus_use = QComboBox()
        self.combo_in_modbus_use.addItems(['analog', 'modbus'])
        self.layout_in_modbus_use.addWidget(self.name_in_modbus_use)
        self.layout_in_modbus_use.addWidget(self.combo_in_modbus_use)
        self.layout_in.addLayout(self.layout_in_modbus_use)

        self.layout_in_type = QHBoxLayout()
        self.name_in_conv = QLabel("Тип ПЧ")
        self.combo_in_type = QComboBox()
        self.combo_in_type.addItems(self.type_conv)
        self.layout_in_type.addWidget(self.name_in_conv)
        self.layout_in_type.addWidget(self.combo_in_type)
        self.layout_in.addLayout(self.layout_in_type)

        self.layout_in_adres = QHBoxLayout()
        self.name_in_id = QLabel("Адрес 1 ПЧ:")
        self.edit_in_id = QLineEdit(str(1))
        self.layout_in_adres.addWidget(self.name_in_id)
        self.layout_in_adres.addWidget(self.edit_in_id)
        self.layout_in.addLayout(self.layout_in_adres)

        self.reserve_in = QHBoxLayout()
        self.name_in_reserve = QLabel("Тип резерва:")
        self.combo_in_reserve = QComboBox()
        self.combo_in_reserve.addItems(self.reserve)
        self.reserve_in.addWidget(self.name_in_reserve)
        self.reserve_in.addWidget(self.combo_in_reserve)
        self.layout_in.addLayout(self.reserve_in)

        self.main_layout.addLayout(self.layout_in)

        self.name_out = QLabel("Вентилятор вытяжка")
        self.layout_out.addWidget(self.name_out)

        self.layout_out_num = QHBoxLayout()
        self.name_out_num = QLabel("Количество")
        self.out_num_edit = QLineEdit('1')
        self.layout_out_num.addWidget(self.name_out_num)
        self.layout_out_num.addWidget(self.out_num_edit)
        self.layout_out.addLayout(self.layout_out_num)

        self.layout_out_modbus_use = QHBoxLayout()
        self.name_out_modbus_use = QLabel("Тип управления")
        self.combo_out_modbus_use = QComboBox()
        self.combo_out_modbus_use.addItems(['analog', 'modbus'])
        self.layout_out_modbus_use.addWidget(self.name_out_modbus_use)
        self.layout_out_modbus_use.addWidget(self.combo_out_modbus_use)
        self.layout_out.addLayout(self.layout_out_modbus_use)

        self.layout_out_type = QHBoxLayout()
        self.name_out_conv = QLabel("Тип ПЧ")
        self.combo_out_type = QComboBox()
        self.combo_out_type.addItems(self.type_conv)
        self.layout_out_type.addWidget(self.name_out_conv)
        self.layout_out_type.addWidget(self.combo_out_type)
        self.layout_out.addLayout(self.layout_out_type)

        self.layout_out_adres = QHBoxLayout()
        self.name_out_id = QLabel("Адрес 1 ПЧ:")
        self.edit_out_id = QLineEdit(str(10))
        self.layout_out_adres.addWidget(self.name_out_id)
        self.layout_out_adres.addWidget(self.edit_out_id)
        self.layout_out.addLayout(self.layout_out_adres)

        self.reserve_out = QHBoxLayout()
        self.name_out_reserve = QLabel("Тип резерва:")
        self.combo_out_reserve = QComboBox()
        self.combo_out_reserve.addItems(self.reserve)
        self.reserve_out.addWidget(self.name_out_reserve)
        self.reserve_out.addWidget(self.combo_out_reserve)
        self.layout_out.addLayout(self.reserve_out)

        self.main_layout.addLayout(self.layout_out)

        self.setLayout(self.main_layout)

        pass
