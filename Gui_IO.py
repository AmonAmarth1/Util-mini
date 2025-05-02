from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout
)

from Literals import Literal

class Gui_IO(QWidget):
    def __init__(self, name_io, config, input_output="input"):
        super().__init__()

        self.config = config
        self.type_io_input = Literal.types_io_input
        self.type_io_output = Literal.types_io_output
        self.type_io_input_product = Literal.types_product_num

        self.name_io = name_io
        self.input_output = input_output

        self.initUI()
    def initUI(self):

        self.layout = QVBoxLayout()

        self.name_io = QLabel(self.name_io)

        self.combo_var_in_digit = QComboBox()
        self.combo_var_in_digit.addItems(list(self.config.Di.keys()))

        self.combo_var_in_analog = QComboBox()
        self.combo_var_in_analog.addItems(list(self.config.Ai.keys()))
        self.combo_var_out_digit = QComboBox()
        self.combo_var_out_digit.addItems(list(self.config.Do.keys()))
        self.combo_var_out_analog = QComboBox()
        self.combo_var_out_analog.addItems(list(self.config.Di.keys()))
        self.combo_var_in_digit.hide()
        self.combo_var_in_analog.hide()
        self.combo_var_out_digit.hide()
        self.combo_var_out_analog.hide()

        self.combo_io_input_type = QComboBox()
        self.combo_io_input_type.addItems(list(self.type_io_input.values()))
        self.combo_io_input_type.currentIndexChanged.connect(self.input_type_changed)

        self.combo_io_output_type = QComboBox()
        self.combo_io_output_type.addItems(list(self.type_io_output.values()))
        self.combo_io_input_type.hide()
        self.combo_io_output_type.hide()

        self.combo_type_io_input_product = QComboBox()
        self.combo_type_io_input_product.addItems(list(self.type_io_input_product.keys()))
        self.combo_type_io_input_product.hide()

        self.layout.addWidget(self.name_io)

        self.layout.addWidget(self.combo_var_in_digit)
        self.layout.addWidget(self.combo_var_in_analog)
        self.layout.addWidget(self.combo_var_out_digit)
        self.layout.addWidget(self.combo_var_out_analog)

        self.layout.addWidget(self.combo_io_input_type)
        self.layout.addWidget(self.combo_io_output_type)
        self.layout.addWidget(self.combo_type_io_input_product)

        self.setLayout(self.layout)
        self.chooseShowComboBox()

    def chooseShowComboBox(self):
        if (self.input_output == "input"):
            type_input = self.combo_io_input_type.currentText()
            self.combo_io_input_type.show()
            self.combo_type_io_input_product.show()
            if(type_input == "Digital"):
                self.combo_var_in_digit.show()
                self.combo_var_in_analog.hide()
            else:
                self.combo_var_in_digit.hide()
                self.combo_var_in_analog.show()
        else:
            type_output = self.combo_io_output_type.currentText()
            self.combo_io_output_type.show()
            if(type_output == "Digital"):
                self.combo_var_out_digit.show()
                self.combo_var_out_analog.hide()
            else:
                self.combo_var_out_digit.hide()
                self.combo_var_out_analog.show()

    def input_type_changed(self):
        self.chooseShowComboBox()

    def get_key(self, d, value):
        for k, v in d.items():
            if v[0] == value:
                return k