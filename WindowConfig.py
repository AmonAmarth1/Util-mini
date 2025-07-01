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
        self.layout.addWidget(CollapsibleWidget(self.layout_heat, 0, 0, 0, 0, "Конфигурация нагревателей, охладителя, камеры смешения"))

        self.layout_sensors = QGridLayout()
        self.widget_sensors_10 = []

        for i in range(0, 10):
            self.widget_sensors_10.append(Gui_sensors(self.config, i + 1))
            self.layout_sensors.addWidget(self.widget_sensors_10[i], int(i / 5), int((i % 5)))
        self.layout.addWidget(
            CollapsibleWidget(self.layout_sensors, 0, 0, 0, 0, "Конфигурация Modbus датчиков"))

        self.layout.addStretch()

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.main_widget.setMinimumSize(1400, 600)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.main_widget)
        self.setLayout(self.main_layout)



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

    def load_function(self):

        if self.data_sourse.currentText() == 'eplan':
            print("load data from eplan")

            if self.eplan_IO != None:

                for i in range(0, len(self.eplan_IO.data_io)):

                    Ui = self.eplan_IO.data_io[i].find("UI")
                    if Ui != -1:
                        index = int(self.eplan_IO.data_io[i][2:])
                        type =  self.eplan_IO.data_io_for_modbus[i][1][0]

                        if type == 2:
                            self.widget_Ui_1_18[index - 1].combo_var_in_digit.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][0][0])
                            self.widget_Ui_1_18[index - 1].combo_io_input_type.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][1][0])

                        else:
                            self.widget_Ui_1_18[index - 1].combo_var_in_analog.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][0][0])
                            self.widget_Ui_1_18[index - 1].combo_io_input_type.setCurrentIndex(self.eplan_IO.data_io_for_modbus[i][1][0])

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
                    else:
                        self.widget_Ui_1_18[i].combo_var_in_analog.setCurrentIndex(self.data_from_plc.Ui_value[i][0])
                    self.widget_Ui_1_18[i].combo_io_input_type.setCurrentIndex(type)
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
