#Кто я и нахер нужен
# с какими данными я связан
# особенности (спорные момента кода, оставленный себе гемсорой)

import sys
import json
import os
import serial.tools.list_ports
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout, QGridLayout, QScrollArea
)

from Test_deepseek import CollapsibleWidget
from Literals import Literal

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
from Gui_Convereter import Gui_Converter
from Gui_heat import Gui_Heat
from Gui_Recup import Gui_Recup
from Gui_dx import Gui_dx
from Gui_Humidifier import Gui_humidifier
from Gui_mix_camera import Gui_mix_camera
from Gui_sensors import Gui_sensors

from PyQt5.QtCore import Qt, QSize
class WindowConfig(QWidget):
    def __init__(self, config, eplan_IO=None, data_from_plc=None):
        super().__init__()
        self.config = config
        self.initUI()

        self.eplan_IO = eplan_IO
        self.eplan_converter = None
        self.eplan_heat = None
        self.eplan_recup = None
        self.eplan_dx = None
        self.eplan_hum = None
        self.eplan_mix = None
        self.eplan_sensors = None

        self.data_from_plc = data_from_plc


    def initUI(self):
        self.setWindowTitle('Config window')
        self.setGeometry(300, 100, 600, 500)

        self.layout = QVBoxLayout()

        self.layout_sourse_data = QHBoxLayout()

        self.data_sourse = QComboBox(self)
        self.data_sourse.addItems(['eplan', 'plc'])
        self.qlabel_text = QLabel("Выбор источника данных для загрузки в окно конфигурации: ")
        self.load_button = QPushButton('Показать данные ', self)
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
            self.widget_Ui_1_18[i].combo_var_in_digit.currentIndexChanged.connect(self.digitChange)
            self.widget_Ui_1_18[i].combo_var_in_analog.currentIndexChanged.connect(self.analogChange)

        for i in range(0, 8):
            self.widget_Uo_1_8.append(Gui_IO(f"Uo{i + 1}", {i}, self.config, "output"))
            self.layout_Out.addWidget(self.widget_Uo_1_8[i], 0, i)

        for i in range(0, 5):
            self.widget_Q_1_5.append(Gui_IO(f"Q{i + 1}", {i}, self.config, "output"))
            self.layout_Out.addWidget(self.widget_Q_1_5[i], 1, i)

        for i in range(0, 2):
            self.widget_T_1_2.append(Gui_IO(f"T{i + 1}", {i}, self.config, "output"))
            self.layout_Out.addWidget(self.widget_T_1_2[i], 2, i)


        self.layout.addWidget(CollapsibleWidget(self.layout_In, 400, 380, 600, 500, "Конфигурация входов Ui"))
        self.layout.addWidget(CollapsibleWidget(self.layout_Out, 400, 300, 600, 500, "Конфигурация выходов Uo, Q, T"))

        self.layout_converter = QHBoxLayout()
        self.converter = Gui_Converter()
        self.recup = Gui_Recup()
        self.layout_converter.addWidget(self.converter)
        self.layout_converter.addWidget(self.recup)
        self.layout.addWidget(CollapsibleWidget(self.layout_converter, 0, 0, 0, 0,"Конфигурация Вентиляторов и рекуператора"))

        self.layout_heat = QHBoxLayout()
        self.heat = Gui_Heat()
        self.dx = Gui_dx()
        self.hum = Gui_humidifier()
        self.mix = Gui_mix_camera()
        self.layout_heat.addWidget(self.heat)
        self.layout_heat.addWidget(self.dx)
        self.layout_heat.addWidget(self.hum)
        self.layout_heat.addWidget(self.mix)
        self.layout.addWidget(CollapsibleWidget(self.layout_heat, 0, 0, 0, 0, "Конфигурация нагревателей, охладителя, увлажнителя и камеры смешения"))

        self.layout_sensors = QGridLayout()
        self.widget_sensors_10 = []

        for i in range(0, 10):
            self.widget_sensors_10.append(Gui_sensors(self.config, i + 1))
            self.layout_sensors.addWidget(self.widget_sensors_10[i], int(i / 5), int((i % 5)))
            self.widget_sensors_10[i].var_combo.currentIndexChanged.connect(self.sensorChange)
        self.layout.addWidget(
            CollapsibleWidget(self.layout_sensors, 0, 0, 0, 0, "Конфигурация Modbus датчиков"))

        self.layout.addStretch()

        self.save_button = QPushButton('Сохранить данные ', self)
        self.save_button.clicked.connect(self.save_function)
        self.layout.addWidget(self.save_button)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.main_widget.setMinimumSize(1400, 600)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.main_widget)
        self.setLayout(self.main_layout)

    def digitChange(self, i):
        num_input_change = 0
        prev_i = 0
        for j in range(0, Literal.IO_LENGTH):
            if i == self.widget_Ui_1_18[j].combo_var_in_digit.currentIndex():
                num_input_change = j
                prev_i = self.widget_Ui_1_18[j].prev_digit
                self.widget_Ui_1_18[j].prev_digit = i
        self.setBlockDigit(i, num_input_change)
        self.resetBlockDigit(prev_i)

    def setBlockDigit(self, i, num_input_change):
        for j in range(0, Literal.IO_LENGTH):
            if(j != num_input_change):
                self.widget_Ui_1_18[j].combo_var_in_digit.model().item(i).setEnabled(False)

    def resetBlockDigit(self, prev_i):
        for j in range(0, Literal.IO_LENGTH):
            self.widget_Ui_1_18[j].combo_var_in_digit.model().item(prev_i).setEnabled(True)

    def analogChange(self, i):
        num_input_change = 0
        prev_i = 0
        for j in range(0, Literal.IO_LENGTH):
            if i == self.widget_Ui_1_18[j].combo_var_in_analog.currentIndex():
                num_input_change = j
                prev_i = self.widget_Ui_1_18[j].prev_analog
                self.widget_Ui_1_18[j].prev_analog = i
        self.setBlockAnalog(i, num_input_change)
        self.resetBlockAnalog(prev_i)

    def setBlockAnalog(self, i, num_input_change):
        for j in range(0, Literal.IO_LENGTH):
            if(j != num_input_change):
                self.widget_Ui_1_18[j].combo_var_in_analog.model().item(i).setEnabled(False)
        for j in range(0, len(self.widget_sensors_10)):
                self.widget_sensors_10[j].var_combo.model().item(i).setEnabled(False)

    def resetBlockAnalog(self, prev_i):
        for j in range(0, Literal.IO_LENGTH):
            self.widget_Ui_1_18[j].combo_var_in_analog.model().item(prev_i).setEnabled(True)
        for j in range(0, len(self.widget_sensors_10)):
            self.widget_sensors_10[j].var_combo.model().item(prev_i).setEnabled(False)

    def sensorChange(self, i):
        num_input_change = 0
        prev_i = 0
        for j in range(0, len(self.widget_sensors_10)):
            if i == self.widget_sensors_10[j].var_combo.currentIndex():
                num_input_change = j
                prev_i = self.widget_sensors_10[j].prev_i
                self.widget_sensors_10[j].prev_i = i
        self.setBlockSens(i, num_input_change)
        self.resetBlockSens(prev_i)

    def setBlockSens(self, i, num_input_change):
        for j in range(0, len(self.widget_sensors_10)):
            if(j != num_input_change):
                self.widget_sensors_10[j].var_combo.model().item(i).setEnabled(False)
        for j in range(0, Literal.IO_LENGTH):
                self.widget_Ui_1_18[j].combo_var_in_analog.model().item(i).setEnabled(False)

    def resetBlockSens(self, prev_i):
        for j in range(0, Literal.IO_LENGTH):
            self.widget_Ui_1_18[j].combo_var_in_analog.model().item(prev_i).setEnabled(True)
        for j in range(0, len(self.widget_sensors_10)):
            self.widget_sensors_10[j].var_combo.model().item(prev_i).setEnabled(False)

    def initIO(self, layout):
        pass

    def setDataFromPLC(self, data_from_plc):
        self.data_from_plc = data_from_plc

    def setDataFromEplanIO(self, data_from_eplan_IO):
        self.eplan_IO = data_from_eplan_IO

    def setDataFromEplanConv(self, data_from_eplan_conv):
        self.eplan_converter = data_from_eplan_conv

    def setDataFromEplanHeat(self, data_from_eplan_heat):
        self.eplan_heat = data_from_eplan_heat

    def setDataFromEplanRecup(self, data_from_eplan_recup):
        self.eplan_recup = data_from_eplan_recup

    def setDataFromEplanDx(self, data_from_eplan_dx):
        self.eplan_dx = data_from_eplan_dx

    def setDataFromEplanHum(self, data_from_eplan_hum):
        self.eplan_hum = data_from_eplan_hum

    def setDataFromEplanMix(self, data_from_eplan_mix):
        self.eplan_mix = data_from_eplan_mix

    def setDataFromEplanSensors(self, data_from_eplan_sensors):
        self.eplan_sensors = data_from_eplan_sensors

    def setDataIOFromGui(self, data_io_from_gui):
        self.data_io_from_gui = data_io_from_gui

    def setDataVentFromGui(self, data_vent_from_gui):
        self.data_vent_from_gui = data_vent_from_gui

    def setDataRecupFromGui(self, data_recup_from_gui):
        self.data_recup_from_gui = data_recup_from_gui

    def setDataHeatFromGui(self, data_heat_from_gui):
        self.data_heat_from_gui = data_heat_from_gui

    def setDataDxFromGui(self, data_dx_from_gui):
        self.data_dx_from_gui = data_dx_from_gui

    def setDataHumFromGui(self, data_hum_from_gui):
        self.data_hum_from_gui = data_hum_from_gui

    def setDataMixFromGui(self, data_mix_from_gui):
        self.data_mix_from_gui = data_mix_from_gui

    def setDataSensorsFromGui(self, data_sensors_from_gui):
        self.data_sensors_from_gui = data_sensors_from_gui

    def load_function(self):

        if self.data_sourse.currentText() == 'eplan':
            print("load data from eplan")

            if self.eplan_IO != None:

                for i in range(0, len(self.eplan_IO.data_io)):

                    Ui = self.eplan_IO.data_io[i].find("UI")
                    if Ui != -1:
                        index = int(self.eplan_IO.data_io[i][2:])
                        type = self.eplan_IO.data_io_for_modbus[i][1][0]

                        if type == 2:
                            self.widget_Ui_1_18[index - 1].combo_var_in_digit.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][0][0])
                            self.widget_Ui_1_18[index - 1].prev_digit = self.eplan_IO.data_io_for_modbus[i][0][0]
                            if index < 7:
                                self.widget_Ui_1_18[index - 1].combo_io_input_type.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][1][0])
                            else:
                                self.widget_Ui_1_18[index - 1].combo_io_input_type.setCurrentIndex(
                                    self.eplan_IO.data_io_for_modbus[i][1][0] - 2)

                        else:
                            self.widget_Ui_1_18[index - 1].combo_var_in_analog.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][0][0])
                            self.widget_Ui_1_18[index - 1].prev_analog = self.eplan_IO.data_io_for_modbus[i][0][0]
                            if index < 7:
                                self.widget_Ui_1_18[index - 1].combo_io_input_type.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][1][0])
                            else:
                                self.widget_Ui_1_18[index - 1].combo_io_input_type.setCurrentIndex(
                                    self.eplan_IO.data_io_for_modbus[i][1][0] - 2)

                        if self.eplan_IO.data_io_for_modbus[i][2][0] != None:
                            self.widget_Ui_1_18[index - 1].combo_type_io_input_product.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][2][0])


                    UO = self.eplan_IO.data_io[i].find("UO")
                    U1 = self.eplan_IO.data_io[i].find("U0")
                    if UO != -1 or U1 != -1:
                        index = int(self.eplan_IO.data_io[i][2:])
                        type = self.eplan_IO.data_io_for_modbus[i][1][0]

                        if type == 17:
                            self.widget_Uo_1_8[index - 1].combo_var_out_digit.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][0][0])
                            self.widget_Uo_1_8[index - 1].combo_io_output_type.setCurrentIndex(2)
                        elif type == 18:
                            self.widget_Uo_1_8[index - 1].combo_var_out_analog.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][0][0])
                            self.widget_Uo_1_8[index - 1].combo_io_output_type.setCurrentIndex(0)
                        else:
                            self.widget_Uo_1_8[index - 1].combo_var_out_analog.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][0][0])
                            self.widget_Uo_1_8[index - 1].combo_io_output_type.setCurrentIndex(1)


                    Q = self.eplan_IO.data_io[i].find("Q")
                    if Q != -1:
                        index = int(self.eplan_IO.data_io[i][1:])
                        self.widget_Q_1_5[index - 1].combo_var_out_digit.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][0][0])


                    T = self.eplan_IO.data_io[i].find("T")
                    if T != -1:
                        index = int(self.eplan_IO.data_io[i][1:])
                        self.widget_T_1_2[index - 1].combo_var_out_digit.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][0][0])

            if self.eplan_converter != None:
                self.converter.in_num_edit.setText(str(self.eplan_converter.getCountInputConverter()))
                self.converter.out_num_edit.setText(str(self.eplan_converter.getCountOutputConverter()))
                self.converter.combo_in_modbus_use.setCurrentIndex(int(self.eplan_converter.getModbusUse()))
                self.converter.combo_out_modbus_use.setCurrentIndex(int(self.eplan_converter.getModbusUse()))
                self.converter.combo_in_type.setCurrentIndex(self.eplan_converter.getTypeCurrecntConverter())
                self.converter.combo_out_type.setCurrentIndex(self.eplan_converter.getTypeCurrecntConverter())

            if self.eplan_heat != None:
                self.heat.heat1_type_combo.setCurrentIndex(self.eplan_heat.heat1_type)
                self.heat.heat2_use_combo.setCurrentIndex(self.eplan_heat.heat2_use)
                self.heat.heat2_type_combo.setCurrentIndex(self.eplan_heat.heat2_type)

                self.recup.recup_use_combo.setCurrentIndex(self.eplan_recup.recup_use)
                self.recup.recup_type_combo.setCurrentIndex(self.eplan_recup.recup_type)

                self.dx.dx_use_combo.setCurrentIndex(self.eplan_dx.dx_use)
                self.dx.type_dx_combo.setCurrentIndex(self.eplan_dx.dx_type)

                self.hum.hum_use_combo.setCurrentIndex(self.eplan_hum.humidifier_use)

                self.mix.mix_use_combo.setCurrentIndex(self.eplan_mix.mix_camera_use)

                j = 0
                for i in range(0, len(self.eplan_sensors.data_for_modbus)):
                    if len(self.eplan_sensors.data_for_modbus[i]) == 3:
                        self.widget_sensors_10[j].id_edit.setText(str(self.eplan_sensors.data_for_modbus[i][0][0]))
                        self.widget_sensors_10[j].type_combo.setCurrentIndex(self.eplan_sensors.data_for_modbus[i][1][0])
                        self.widget_sensors_10[j].var_combo.setCurrentIndex(self.eplan_sensors.data_for_modbus[i][2][0])
                        j = j + 1
                    if len(self.eplan_sensors.data_for_modbus[i]) == 6:
                        self.widget_sensors_10[j].id_edit.setText(str(self.eplan_sensors.data_for_modbus[i][0][0]))
                        self.widget_sensors_10[j].type_combo.setCurrentIndex(self.eplan_sensors.data_for_modbus[i][1][0])
                        self.widget_sensors_10[j].var_combo.setCurrentIndex(self.eplan_sensors.data_for_modbus[i][2][0])
                        self.widget_sensors_10[j + 1].id_edit.setText(str(self.eplan_sensors.data_for_modbus[i][3][0]))
                        self.widget_sensors_10[j + 1].type_combo.setCurrentIndex(self.eplan_sensors.data_for_modbus[i][4][0])
                        self.widget_sensors_10[j + 1].var_combo.setCurrentIndex(self.eplan_sensors.data_for_modbus[i][5][0])
                        j = j + 2
        else:
            print("load data from plc")

            if self.data_from_plc != None:
                for i in range(0, len(self.data_from_plc.Ui_value)):
                    type = self.data_from_plc.Ui_value[i][1]

                    if type == 2:
                        self.widget_Ui_1_18[i].combo_var_in_digit.setCurrentIndex(self.data_from_plc.Ui_value[i][0])
                        self.widget_Ui_1_18[i].prev_digit = self.data_from_plc.Ui_value[i][0]
                    else:
                        self.widget_Ui_1_18[i].combo_var_in_analog.setCurrentIndex(self.data_from_plc.Ui_value[i][0])
                        self.widget_Ui_1_18[i].prev_analog = self.data_from_plc.Ui_value[i][0]
                    if i < 6:
                        self.widget_Ui_1_18[i].combo_io_input_type.setCurrentIndex(type)
                    else:
                        self.widget_Ui_1_18[i].combo_io_input_type.setCurrentIndex(type - 2)
                    self.widget_Ui_1_18[i].combo_type_io_input_product.setCurrentIndex(self.data_from_plc.Ui_value[i][2])

                    if type < 2:
                        self.widget_Ui_1_18[i].line_edit_min.setText(str(self.data_from_plc.Ui_value[i][3]))
                        self.widget_Ui_1_18[i].line_edit_min.setText(str(self.data_from_plc.Ui_value[i][4]))

                for i in range(0, len(self.data_from_plc.Uo_value)):
                    type = self.data_from_plc.Uo_value[i][1]

                    if type == 17:
                        self.widget_Uo_1_8[i].combo_var_out_digit.setCurrentIndex(self.data_from_plc.Uo_value[i][0])
                        self.widget_Uo_1_8[i].combo_io_output_type.setCurrentIndex(2)
                    elif type == 18:
                        self.widget_Uo_1_8[i].combo_var_out_analog.setCurrentIndex(self.data_from_plc.Uo_value[i][0])
                        self.widget_Uo_1_8[i].combo_io_output_type.setCurrentIndex(0)
                        self.widget_Uo_1_8[i].line_edit_period.setText(str(self.data_from_plc.Uo_value[i][2]))
                    else:
                        self.widget_Uo_1_8[i].combo_var_out_analog.setCurrentIndex(self.data_from_plc.Uo_value[i][0])
                        self.widget_Uo_1_8[i].combo_io_output_type.setCurrentIndex(1)
                        self.widget_Uo_1_8[i].line_edit_period.setText(str(self.data_from_plc.Uo_value[i][2]))

                for i in range(0, len(self.data_from_plc.Q_value)):
                    self.widget_Q_1_5[i].combo_var_out_digit.setCurrentIndex(self.data_from_plc.Q_value[i][0])

                for i in range(0, len(self.data_from_plc.T_value)):
                    self.widget_T_1_2[i].combo_var_out_digit.setCurrentIndex(self.data_from_plc.T_value[i][0])

                self.converter.in_num_edit.setText(str(self.data_from_plc.converter_data[2]))
                self.converter.out_num_edit.setText(str(self.data_from_plc.converter_data[3]))
                self.converter.combo_in_modbus_use.setCurrentIndex(self.data_from_plc.converter_data[0])
                self.converter.combo_out_modbus_use.setCurrentIndex(self.data_from_plc.converter_data[1])
                self.converter.combo_in_type.setCurrentIndex(self.data_from_plc.converter_data[4])
                self.converter.combo_out_type.setCurrentIndex(self.data_from_plc.converter_data[5])
                self.converter.edit_in_id.setText(str(self.data_from_plc.converter_data[8]))
                self.converter.edit_out_id.setText(str(self.data_from_plc.converter_data[9]))
                self.converter.combo_in_reserve.setCurrentIndex(self.data_from_plc.converter_data[6])
                self.converter.combo_out_reserve.setCurrentIndex(self.data_from_plc.converter_data[7])

                self.heat.heat1_type_combo.setCurrentIndex(self.data_from_plc.heat_data[0])
                self.heat.heat1_reserve_pump_combo.setCurrentIndex(self.data_from_plc.heat_data[3])
                self.heat.heat2_use_combo.setCurrentIndex(self.data_from_plc.heat_data[1])
                self.heat.heat2_type_combo.setCurrentIndex(self.data_from_plc.heat_data[2])
                self.heat.heat2_reserve_pump_combo.setCurrentIndex(self.data_from_plc.heat_data[4])

                self.recup.recup_use_combo.setCurrentIndex(self.data_from_plc.recup_data[0])
                self.recup.recup_type_combo.setCurrentIndex(self.data_from_plc.recup_data[1])
                self.recup.recup_modbus_use_combo.setCurrentIndex(self.data_from_plc.recup_data[2])
                self.recup.recup_id_edit.setText(str(self.data_from_plc.recup_data[3]))
                self.recup.recup_rpm_edit.setText(str(self.data_from_plc.recup_data[4]))
                self.recup.recup_conv_type_combo.setCurrentIndex(self.data_from_plc.recup_data[5])

                self.dx.dx_use_combo.setCurrentIndex(self.data_from_plc.dx_data[0])
                self.dx.type_dx_combo.setCurrentIndex(self.data_from_plc.dx_data[1])
                self.dx.dx_heat_combo.setCurrentIndex(self.data_from_plc.dx_data[2])

                self.hum.hum_use_combo.setCurrentIndex(self.data_from_plc.humidifier_data[0])

                self.mix.mix_use_combo.setCurrentIndex(self.data_from_plc.mix_camera_data[0])

                for i in range(0, len(self.data_from_plc.id_list)):
                    self.widget_sensors_10[i].id_edit.setText(str(self.data_from_plc.id_list[i]))
                    self.widget_sensors_10[i].type_combo.setCurrentIndex(self.data_from_plc.sensors_type_list_raw[i])
                    self.widget_sensors_10[i].var_combo.setCurrentIndex(self.data_from_plc.sensors_var_list_raw[i])

    def save_function(self):
        self.data_io_from_gui.clear()
        for i in range(0, 18):
            if i < 6:
                type = self.widget_Ui_1_18[i].combo_io_input_type.currentIndex()
            else:
                type = self.widget_Ui_1_18[i].combo_io_input_type.currentIndex() + 2
            if type != 2:
                self.data_io_from_gui.var.append(self.widget_Ui_1_18[i].combo_var_in_analog.currentIndex())
            else:
                self.data_io_from_gui.var.append(self.widget_Ui_1_18[i].combo_var_in_digit.currentIndex())
            self.data_io_from_gui.method.append(self.widget_Ui_1_18[i].combo_type_io_input_product.currentIndex())
            if (i < 6):
                self.data_io_from_gui.type.append(2 if self.widget_Ui_1_18[i].combo_io_input_type.currentIndex() == -1 else self.widget_Ui_1_18[i].combo_io_input_type.currentIndex())
                try:
                    self.data_io_from_gui.min.append(0 if self.widget_Ui_1_18[i].line_edit_min.text() == '' else int(self.widget_Ui_1_18[i].line_edit_min.text()))
                    self.data_io_from_gui.max.append(0 if self.widget_Ui_1_18[i].line_edit_max.text() == '' else int(self.widget_Ui_1_18[i].line_edit_max.text()))
                except Exception:
                    print("Min, max trash!!!!")
                    self.data_io_from_gui.min.append(0)
                    self.data_io_from_gui.max.append(0)
            else:
                self.data_io_from_gui.type.append(2 if self.widget_Ui_1_18[i].combo_io_input_type.currentIndex() == -1 else self.widget_Ui_1_18[i].combo_io_input_type.currentIndex() + 2)

        self.data_io_from_gui.setAnalogUseBit()

        for i in range(0, 5):
            self.data_io_from_gui.Q_var.append(self.widget_Q_1_5[i].combo_var_out_digit.currentIndex())
        for i in range(0, 2):
            self.data_io_from_gui.T_var.append(self.widget_T_1_2[i].combo_var_out_digit.currentIndex())
        print(self.data_io_from_gui.Q_var)
        print(self.data_io_from_gui.T_var)

        for i in range(0, 8):
            type = self.widget_Uo_1_8[i].combo_io_output_type.currentIndex()
            type2 = 0
            if type == 2:
                type2 = 17
                self.data_io_from_gui.U_var.append(self.widget_Uo_1_8[i].combo_var_out_digit.currentIndex())
            elif type == 1:
                type2 = 19
                self.data_io_from_gui.U_var.append(self.widget_Uo_1_8[i].combo_var_out_analog.currentIndex())
            else:
                type2 = 18
                self.data_io_from_gui.U_var.append(self.widget_Uo_1_8[i].combo_var_out_analog.currentIndex())
            self.data_io_from_gui.U_type.append(type2)
            self.data_io_from_gui.U_period.append(0 if self.widget_Uo_1_8[i].line_edit_period.text() == '' else int(self.widget_Uo_1_8[i].line_edit_period.text()))


        self.data_io_from_gui.setDigitUseBit()
        self.data_io_from_gui.makeDataIOModbus()

        print(self.data_io_from_gui.getDataModbus())

        self.data_vent_from_gui.vent_in_num = int(self.converter.in_num_edit.text())
        self.data_vent_from_gui.vent_out_num = int(self.converter.out_num_edit.text())

        self.data_vent_from_gui.vent_in_modbus_use = self.converter.combo_in_modbus_use.currentIndex()
        self.data_vent_from_gui.vent_out_modbus_use= self.converter.combo_out_modbus_use.currentIndex()

        self.data_vent_from_gui.vent_in_type = self.converter.combo_in_type.currentIndex()
        self.data_vent_from_gui.vent_out_type = self.converter.combo_out_type.currentIndex()

        self.data_vent_from_gui.vent_in_id = int(self.converter.edit_in_id.text())
        self.data_vent_from_gui.vent_out_id = int(self.converter.edit_out_id.text())

        self.data_vent_from_gui.vent_in_reserve = self.converter.combo_in_reserve.currentIndex()
        self.data_vent_from_gui.vent_out_reserve = self.converter.combo_out_reserve.currentIndex()

        self.data_vent_from_gui.makeDataModebus()

        print(self.data_vent_from_gui.modbus_data)

        self.data_recup_from_gui.recup_use = self.recup.recup_use_combo.currentIndex()
        self.data_recup_from_gui.type = self.recup.recup_type_combo.currentIndex()
        self.data_recup_from_gui.modbus_use = self.recup.recup_modbus_use_combo.currentIndex()
        self.data_recup_from_gui.id = int(self.recup.recup_id_edit.text())
        self.data_recup_from_gui.recup_rpm = int(self.recup.recup_rpm_edit.text())
        self.data_recup_from_gui.type_conv = self.recup.recup_conv_type_combo.currentIndex()
        self.data_recup_from_gui.makeDataModbus()

        print(self.data_recup_from_gui.getDataModbus())

        self.data_heat_from_gui.heat1_type = self.heat.heat1_type_combo.currentIndex()
        self.data_heat_from_gui.heat1_reserve_pump = self.heat.heat1_reserve_pump_combo.currentIndex()
        self.data_heat_from_gui.heat2_use = self.heat.heat2_use_combo.currentIndex()
        self.data_heat_from_gui.heat2_type = self.heat.heat2_type_combo.currentIndex()
        self.data_heat_from_gui.heat2_reserve_pump = self.heat.heat2_reserve_pump_combo.currentIndex()
        self.data_heat_from_gui.makeDataModbus()

        print(self.data_heat_from_gui.getDataModbus())

        self.data_dx_from_gui.dx_use = self.dx.dx_use_combo.currentIndex()
        self.data_dx_from_gui.dx_type = self.dx.type_dx_combo.currentIndex()
        self.data_dx_from_gui.dx_heat_use = self.dx.dx_heat_combo.currentIndex()
        self.data_dx_from_gui.makeDataModbus()

        print(self.data_dx_from_gui.getDataModbus())

        self.data_hum_from_gui.hum_use = self.hum.hum_use_combo.currentIndex()
        self.data_hum_from_gui.makeDataModbus()

        print(self.data_hum_from_gui.getDataModbus())

        self.data_mix_from_gui.mix_use = self.mix.mix_use_combo.currentIndex()
        self.data_mix_from_gui.makeDataModbus()

        print(self.data_mix_from_gui.getDataModbus())

        self.data_sensors_from_gui.clear()

        self.data_sensors_from_gui.analog_bit_access_io = self.data_io_from_gui.analog_bit_access

        for i in range(0, len(self.widget_sensors_10)):
            self.data_sensors_from_gui.id.append(int(self.widget_sensors_10[i].id_edit.text()))
            self.data_sensors_from_gui.type.append(self.widget_sensors_10[i].type_combo.currentIndex())
            self.data_sensors_from_gui.var.append(self.widget_sensors_10[i].var_combo.currentIndex())

        print("sensors")
        print(self.data_sensors_from_gui.id)
        print(self.data_sensors_from_gui.type)
        print(self.data_sensors_from_gui.var)

        self.data_sensors_from_gui.makeDataModbus()

        print(self.data_sensors_from_gui.getDataModbus())

        print("Save data!!!!")