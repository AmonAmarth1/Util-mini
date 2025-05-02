import sys
import json
import os
import serial.tools.list_ports
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout, QGridLayout, QScrollArea
)



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
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.initUI()


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

        self.layout_IO = QGridLayout()
        self.widget_IO_1_18 = []

        for i in range(0, 18):

            self.widget_IO_1_18.append(Gui_IO(f"Ui{i + 1}", self.config, "input"))
            self.layout_IO.addWidget(self.widget_IO_1_18[i], int(i / 6), int((i % 6)))

        self.layout.addLayout(self.layout_IO)

        self.scroll.setLayout(self.layout)

        self.setLayout(self.layout)



    def initIO(self, layout):
        pass

    def load_function(self):

        pass

