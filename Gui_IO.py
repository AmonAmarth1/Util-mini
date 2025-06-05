from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout, QLineEdit
)

from Literals import Literal

class Gui_IO(QWidget):
    def __init__(self, name_io, num, config, input_output="input"):
        super().__init__()

        self.config = config
        self.num = num

        self.type_io_input = Literal.types_io_input
        self.type_io_output = Literal.types_io_output
        self.type_io_output_2 = Literal.types_io_output_2
        self.type_io_input_product = Literal.types_product_num

        self.name_io = name_io
        self.input_output = input_output
        self.type = 0

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
        self.combo_var_out_analog.addItems(list(self.config.Ao.keys()))

        self.combo_var_in_digit.hide()
        self.combo_var_in_analog.hide()
        self.combo_var_out_digit.hide()
        self.combo_var_out_analog.hide()

        self.combo_io_input_type = QComboBox()

        name = self.name_io.text()
        if (name == "Ui1" or name == "Ui2" or name == "Ui3" or name == "Ui4" or name == "Ui5" or name == "Ui6"):
            self.line_edit_min = QLineEdit()
            self.line_edit_max = QLineEdit()
            self.combo_io_input_type.addItems(list(self.type_io_input.values()))
        else:
            self.combo_io_input_type.addItem('--')
            self.combo_io_input_type.addItem('--')
            self.combo_io_input_type.addItem(self.type_io_input[2])
            self.combo_io_input_type.addItem(self.type_io_input[3])
            self.combo_io_input_type.setCurrentIndex(2)
        self.combo_io_input_type.currentIndexChanged.connect(self.input_type_changed)

        self.Digital_output_Q = self.name_io.text().find("Q")
        self.Digital_output_T = self.name_io.text().find("T")
        self.combo_io_output_type = QComboBox()

        if (self.Digital_output_Q != -1 or self.Digital_output_T != -1):
            values = list(self.type_io_output.values())
            print(values)
            self.combo_io_output_type.addItem(values[2])
        else:
            self.combo_io_output_type.addItems(list(self.type_io_output_2.values()))

        self.combo_io_output_type.currentIndexChanged.connect(self.input_type_changed)

        self.output_Uo = self.name_io.text().find("Uo")

        if (self.output_Uo != -1):
            self.line_edit_period = QLineEdit()
            self.line_edit_period.hide()

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

        if (name == "Ui1" or name == "Ui2" or name == "Ui3" or name == "Ui4" or name == "Ui5" or name == "Ui6"):
            self.layout.addWidget(self.line_edit_min)
            self.layout.addWidget(self.line_edit_max)
            self.line_edit_min.hide()
            self.line_edit_max.hide()

        if (self.output_Uo != -1):
            self.layout.addWidget(self.line_edit_period)
        self.setLayout(self.layout)
        self.chooseShowComboBox()

    def chooseShowComboBox(self):
        if (self.input_output == "input"):
            type_input = self.combo_io_input_type.currentText()
            self.combo_io_input_type.show()
            self.combo_type_io_input_product.show()
            name = self.name_io.text()
            if(type_input == "Digital"):
                self.combo_var_in_digit.show()
                self.combo_var_in_analog.hide()
                if (name == "Ui1" or name == "Ui2" or name == "Ui3" or name == "Ui4" or name == "Ui5" or name == "Ui6"):
                    self.line_edit_min.hide()
                    self.line_edit_max.hide()
                    pass
            elif (type_input == "Resistance"):
                self.combo_var_in_digit.hide()
                self.combo_var_in_analog.show()
                if (name == "Ui1" or name == "Ui2" or name == "Ui3" or name == "Ui4" or name == "Ui5" or name == "Ui6"):
                    self.line_edit_min.hide()
                    self.line_edit_max.hide()
                    pass
            else:
                self.combo_var_in_digit.hide()
                self.combo_var_in_analog.show()
                if (name == "Ui1" or name == "Ui2" or name == "Ui3" or name == "Ui4" or name == "Ui5" or name == "Ui6"):
                    self.line_edit_min.show()
                    self.line_edit_max.show()

        else:
            type_output = self.combo_io_output_type.currentText()
            self.combo_io_output_type.show()
            if(type_output == "Digital"):
                self.combo_var_out_analog.hide()
                self.combo_var_out_digit.show()
                if (self.output_Uo != -1):
                    self.line_edit_period.hide()
            elif(type_output == "0-10V"):
                self.combo_var_out_analog.show()
                self.combo_var_out_digit.hide()
                if (self.output_Uo != -1):
                    self.line_edit_period.hide()
            else:
                self.combo_var_out_digit.hide()
                self.combo_var_out_analog.show()
                if (self.output_Uo != -1):
                    self.line_edit_period.show()

    def input_type_changed(self):
        self.chooseShowComboBox()

    def get_key(self, d, value):
        for k, v in d.items():
            if v[0] == value:
                return k

    def set_type(self, type, data_from_plc):
        self.data_from_plc = data_from_plc
        if(self.input_output == "input"):
            self.combo_io_input_type.setCurrentIndex(type)
            self.type = type
        else:
            if (self.Digital_output_Q != -1 or self.Digital_output_T != -1):
                pass
            else:
                self.combo_io_output_type.setCurrentIndex(type - 17)
            self.type = type

    def set_var(self, var):
        if (self.input_output == "input"):
            if(self.type == 2):
                self.combo_var_in_digit.setCurrentIndex(var)
            else:
                self.combo_var_in_analog.setCurrentIndex(var)
        else:
            self.combo_io_output_type.setCurrentIndex(type)