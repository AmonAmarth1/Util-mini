import sys
import json
import os
import serial.tools.list_ports
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout, QGridLayout, QScrollArea
)

from Test_deepseek import CollapsibleWidget

from Config import Config
from DataFromEplan import DataFromEplan
from ControllerIO import ControllerIO
from ControllerConverter import ControllerConverter
from ControllerHeat import ControllerHeat
from ControllerRecup import ControllerRecup
from ControllerDx import ControllerDx
from ControllerHumidifer import ControllerHumidifier
from ControllerMixCamera import ControllerMixCamera
from ControllerModbusSensor import ControllerModbusSensor

from DataFileSave import DataFileSave

from DataForPLC import DataPLC
from DriverModbusWriteDataPLC import DriverModbusWriteDataPLC
from DataFromPLC import DataFromPLC

from Gui_IO import Gui_IO
from PyQt5.QtCore import Qt, QSize
class WindowConfig(QWidget):
    def __init__(self, config, eplan_IO, data_plc=None):
        super().__init__()
        self.config = config
        self.initUI()

        self.eplan_IO = eplan_IO
        self.data_from_plc = data_plc

    def initUI(self):
        self.setWindowTitle('Config window')
        self.setGeometry(300, 100, 600, 500)

        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)


        self.layout = QVBoxLayout()

        self.layout_sourse_data = QHBoxLayout()

        self.data_sourse = QComboBox(self)
        self.data_sourse.addItems(['eplan', 'plc'])
        self.qlabel_text = QLabel("Выбор источника данных для загрузки в окно конфигурации: ")
        self.load_button = QPushButton('Загрузить данные ', self)
        self.load_button.clicked.connect(self.load_function)

        self.layout_sourse_data.addWidget(self.qlabel_text)
        self.layout_sourse_data.addWidget(self.data_sourse)
        self.layout_sourse_data.addWidget(self.load_button)

        self.layout.addLayout(self.layout_sourse_data)

        self.layout_In = QGridLayout()
        self.widget_Ui_1_18 = []

        self.layout_Out = QGridLayout()
        self.widget_Uo_1_8 = []
        self.widget_Q_1_5 = []
        self.widget_T_1_2 = []

        for i in range(0, 18):
            self.widget_Ui_1_18.append(Gui_IO(f"Ui{i + 1}", {i}, self.config, "input"))
            self.layout_In.addWidget(self.widget_Ui_1_18[i], int(i / 6), int((i % 6)))

        for i in range(0, 8):
            self.widget_Uo_1_8.append(Gui_IO(f"Uo{i + 1}", {i}, self.config, "output"))
            self.layout_Out.addWidget(self.widget_Uo_1_8[i], 0, i)

        for i in range(0, 5):
            self.widget_Q_1_5.append(Gui_IO(f"Q{i + 1}", {i}, self.config, "output"))
            self.layout_Out.addWidget(self.widget_Q_1_5[i], 1, i)

        for i in range(0, 2):
            self.widget_T_1_2.append(Gui_IO(f"T{i + 1}", {i}, self.config, "output"))
            self.layout_Out.addWidget(self.widget_T_1_2[i], 2, i)


        self.layout.addWidget(CollapsibleWidget(self.layout_In, "Конфигурация входов Ui"))
        self.layout.addWidget(CollapsibleWidget(self.layout_Out, "Конфигурация выходов Uo, Q, T"))
        self.layout.addStretch()

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.main_widget.setMinimumSize(1400, 600)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.main_widget)
        self.setLayout(self.main_layout)



    def initIO(self, layout):
        pass

    def load_function(self):

        if self.data_sourse.currentText() == 'eplan':
            print("load data eplan")
            for i in range (0, len(self.eplan_IO.data_io)):
                Ui = self.eplan_IO.data_io[i].find("UI")
                if Ui != -1:
                    index = int(self.eplan_IO.data_io[i][2:])
                    self.widget_Ui_1_18[index - 1].combo_var_in_digit.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][0][0])
                    type =  self.eplan_IO.data_io_for_modbus[i][1][0]
                    if type == 2:
                        self.widget_Ui_1_18[index - 1].combo_var_in_digit.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][0][0])
                        self.widget_Ui_1_18[index - 1].combo_io_input_type.setCurrentIndex(2)
                    else:
                        self.widget_Ui_1_18[index - 1].combo_var_in_analog.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][0][0])
                        self.widget_Ui_1_18[index - 1].combo_io_input_type.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][1][0])

                UO = self.eplan_IO.data_io[i].find("UO")
                Q = self.eplan_IO.data_io[i].find("Q")
                T = self.eplan_IO.data_io[i].find("T")
                pass
        else:
            print("load data plc")


        pass

