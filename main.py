import sys
import json
import os
import serial.tools.list_ports
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QLabel, QTextEdit, QHBoxLayout
)

import Modbus_rtu
from Modbus_rtu import create_modbus_rtu_packet

CONFIG_FILE = 'config.json'

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

from WindowConfig import WindowConfig

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_config()  # Загружаем конфигурацию при запуске

    def initUI(self):
        self.setWindowTitle('Util mini')
        self.setGeometry(100, 100, 700, 800)

        layout = QVBoxLayout()

        # Кнопка для выбора файла
        self.file_button_specification = QPushButton('Выбрать файл eplan Спецификация', self)
        self.file_button_specification.clicked.connect(self.choose_file_specification)
        layout.addWidget(self.file_button_specification)

        # Кнопка для выбора файла eplan
        self.file_button_scheme_plc = QPushButton('Выбрать файл eplan Схема ПЛК', self)
        self.file_button_scheme_plc.clicked.connect(self.choose_file_scheme_plc)
        layout.addWidget(self.file_button_scheme_plc)

        # Выпадающий список "порт"
        self.port_combo = QComboBox(self)
        self.port_combo.addItems(self.get_serial_ports())

        # Выпадающий список "скорость"
        self.baudrate_combo = QComboBox(self)
        self.baudrate_combo.addItems(['9600', '14400', '19200', '38400', '57600', '115200'])

        # Выпадающий список "четность"
        self.parity_combo = QComboBox(self)
        self.parity_combo.addItems(['None', 'Even', 'Odd'])


        # Выпадающий список "ID"
        self.id_combo = QComboBox(self)
        self.id_combo.addItems(["Id " + str(x) for x in range(1, 255)])

        layout_Hbox = QHBoxLayout()
        layout_Hbox.addWidget(self.port_combo)
        layout_Hbox.addWidget(self.baudrate_combo)
        layout_Hbox.addWidget(self.parity_combo)
        layout_Hbox.addWidget(self.id_combo)
        layout.addLayout(layout_Hbox)


        # Кнопка "загрузить"
        self.load_button = QPushButton('Загрузить данные из eplan', self)
        self.load_button.clicked.connect(self.load_function)
        layout.addWidget(self.load_button)

        self.load_button_plc = QPushButton('Загрузить данные из PLC', self)
        self.load_button_plc.clicked.connect(self.load_function_plc)
        layout.addWidget(self.load_button_plc)

        self.qlabel_text = QLabel("Выбро источника для сохранения данных в файл: ")

        # Выпадающий список "источник для сохранения данных"
        self.sourse_data = QComboBox(self)
        self.sourse_data.addItems(['Eplan', 'PLC'])

        layout_Hbox1 = QHBoxLayout()
        layout_Hbox1.addWidget(self.qlabel_text)
        layout_Hbox1.addWidget(self.sourse_data)
        layout.addLayout(layout_Hbox1)

        # Кнопка "выгрузить"
        self.unload_button = QPushButton('Сохранить данные в файл', self)
        self.unload_button.clicked.connect(self.unload_function_file)
        layout.addWidget(self.unload_button)

        self.unload_button_plc = QPushButton('Выгрузить данные в плк', self)
        self.unload_button_plc.clicked.connect(self.unload_function_plc)
        layout.addWidget(self.unload_button_plc)

        # Поле для вывода информации
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        # Кнопка "Очистить"
        self.clear_button = QPushButton('Очистить', self)
        self.clear_button.clicked.connect(self.clear_function)
        layout.addWidget(self.clear_button)

        self.config_window = QPushButton('Открыть окно конфигурации', self)
        self.config_window.clicked.connect(self.open_config_window)
        layout.addWidget(self.config_window)

        self.setLayout(layout)

        self.config = Config()
        self.dataFromEplan = DataFromEplan()
        self.controllerIO = ControllerIO(self.config)
        self.controllerConverter = ControllerConverter()
        self.controllerHeat = ControllerHeat()
        self.contollerRecup = ControllerRecup()
        self.contollerDx = ControllerDx()
        self.contollerHumidifier = ControllerHumidifier()
        self.controllerMixCamera = ControllerMixCamera()
        self.contollerModbusSensors = ControllerModbusSensor()
        self.dataPLC = DataPLC()


        self.dataSaveFile = DataFileSave()
        # тут вызывать функцию конфиг
        # config = твой клас конфига

        self.data_base = {}

        try:
            self.config.readExel('conf.xlsx')
        except Exception:
            print("Ошибка загрузки conf!!!!!!!!")
            self.output_text.append("Ошибка загрузки conf!!!!!!!!")
        else:
            self.config.printDictionary()
            self.output_text.append('Conf загружен.')

    def choose_file_specification(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "All Files (*);;Text Files (*.txt)",
                                                   options=options)
        if file_path:
            self.file_button_specification.setText(file_path)  # Изменяем текст кнопки на путь к файлу
            self.output_text.append(f'Выбранный файл: {file_path}')
            print('выбран файл')

    def choose_file_scheme_plc(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "All Files (*);;Text Files (*.txt)",
                                                   options=options)
        if file_path:
            self.file_button_scheme_plc.setText(file_path)  # Изменяем текст кнопки на путь к файлу
            self.output_text.append(f'Выбранный файл: {file_path}')
            print('выбран файл')

    def load_function(self):
        # Здесь разместите код для загрузки

        data = create_modbus_rtu_packet(slave_address=1, function='read', data_area='holding', starting_address=1, quantity_of_data=5)
        #self.output_text.append(' '.join([hex(b)[2:].zfill(2).upper() for b in data]))

        file_path_scheme_plc = self.file_button_scheme_plc.text()
        self.dataFromEplan.clear()

        try:
            self.dataFromEplan.readExel_scheme_plc(file_path_scheme_plc)
        except Exception:
            print("Ошибка загрузки схемы плк!!!!!!")
            self.output_text.append("Ошибка загрузки схемы плк!!!!!!")
        else:
            self.dataFromEplan.print_scheme_plc()

        file_path_specification = self.file_button_specification.text()

        try:
            self.dataFromEplan.readExel_specification(file_path_specification)
        except Exception:
            print("Ошибка загрузки спецификации!!!!!!")
            self.output_text.append("Ошибка загрузки спецификации!!!!!!")
        else:
            self.dataFromEplan.makeData()

        self.controllerConverter.makeDataModbus(self.dataFromEplan.getNameVarScheme(), self.dataFromEplan.getNameVarSpecification(), self.dataFromEplan.getProductNumber())
        self.controllerHeat.makeDataModbus(self.dataFromEplan.getNameVarScheme())
        self.contollerRecup.makeDataModbus(self.dataFromEplan.getNameVarScheme())
        self.contollerDx.makeDataModbus(self.dataFromEplan.getNameVarScheme())
        self.contollerHumidifier.makeDataModbus(self.dataFromEplan.getNameVarScheme())
        self.controllerMixCamera.makeDataModbus(self.dataFromEplan.getNameVarScheme())
        self.contollerModbusSensors.makeDataModbus(self.dataFromEplan.getNameVarSpecification(), self.dataFromEplan.getProductNumber())


        self.dataPLC.clear()
        try:
            for i in range(0, self.dataFromEplan.getFileLengthSchemePlc()):
                self.dataPLC.addDataIOModbus(self.controllerIO.getValueAndReg(self.dataFromEplan.getVar(i), self.dataFromEplan.getIO(i), self.dataFromEplan.getProduct_number_IO(i)))
                self.dataPLC.addDataVarIO(self.controllerIO.getNameVarPlC(self.dataFromEplan.getVar(i)))
                self.dataPLC.addDataIO(self.dataFromEplan.getIO(i))
        except Exception:
            print("Ошибка обработки данных!!!!!!")
            self.output_text.append("Ошибка обработки данных!!!!!!")
        self.dataPLC.setAnalogBitAcess(self.controllerIO.analog_bit_access | self.contollerModbusSensors.analog_bit_access)
        self.dataPLC.setBinDigital()
        self.dataPLC.print()
        self.output_text.append("Данные conf и excel загружены...")

    def load_function_plc(self):
        print("Загрузка данных из плк.")
        try:
            self.data_from_plc = DataFromPLC(self.config, int(self.id_combo.currentText().replace("Id ", "")), self.port_combo.currentText(), int(self.baudrate_combo.currentText()), 8, self.parity_combo.currentText()[:1])
            self.data_from_plc.readAllData()
        except Exception as e:
            self.output_text.append(f"Произошло исключение: {e}")
            print(f"Произошло исключение: {e}")
        else:
            self.data_from_plc.print()
            self.output_text.append("Данные из плк загружены.")
        pass

    def unload_function_file(self):
        try:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "All Files (*);;Text Files (*.txt)",
                                                       options=options)
            if file_path:
                print('выбран файл сохранения')
                self.output_text.append(f'Выбранный файл для сохранения: {file_path}')

                sourse = self.sourse_data.currentText()

                if (sourse == 'Eplan'):

                    self.dataSaveFile.setIOData(self.dataPLC.getDataIO(), self.dataPLC.getDataVar(), self.dataPLC.getDataModbus())
                    self.dataSaveFile.setConverterData(self.controllerConverter.getCountInputConverter(), self.controllerConverter.getCountOutputConverter(), self.controllerConverter.getModbusUse(), self.controllerConverter.type_current_converter_name, self.controllerConverter.getDataForModbus())
                    self.dataSaveFile.setHeatData(self.controllerHeat.heat1_type_name, self.controllerHeat.heat2_use, self.controllerHeat.heat2_type_name, self.controllerHeat.getDataForModbus())
                    self.dataSaveFile.setRecupData(self.contollerRecup.recup_use, self.contollerRecup.recup_type_name, self.contollerRecup.getDataForModbus())
                    self.dataSaveFile.setDxData(self.contollerDx.dx_use, self.contollerDx.dx_type_name, self.contollerDx.getDataForModbus())
                    self.dataSaveFile.setHumidifierData(self.contollerHumidifier.humidifier_use, self.contollerHumidifier.getDataForModbus())
                    self.dataSaveFile.setMixCameraData(self.controllerMixCamera.mix_camera_use, self.controllerMixCamera.getDataForModbus())
                    self.dataSaveFile.setModbusSensorsData(self.contollerModbusSensors.name_using_sensors, self.contollerModbusSensors.name_type_sensors, self.contollerModbusSensors.name_var_using_sensors, 'eplan', 0, self.contollerModbusSensors.getDataForModbus())
                    self.dataSaveFile.createFile(file_path, 'eplan')
                    self.output_text.append(f"Сохранение данных из eplan выполнено успешно...")

                else:

                    self.dataSaveFile.setIOData(self.data_from_plc.data_io, self.data_from_plc.data_io_var)
                    self.dataSaveFile.setConverterData(self.data_from_plc.converter_data[2], self.data_from_plc.converter_data[3], self.data_from_plc.converter_data[0], self.data_from_plc.converter_type)
                    self.dataSaveFile.setHeatData(self.data_from_plc.type_heat1, self.data_from_plc.heat_data[1], self.data_from_plc.type_heat2)
                    self.dataSaveFile.setRecupData(self.data_from_plc.recup_data[0], self.data_from_plc.recup_type)
                    self.dataSaveFile.setDxData(self.data_from_plc.dx_data[0], self.data_from_plc.type_dx)
                    self.dataSaveFile.setHumidifierData(self.data_from_plc.humidifier_data[0])
                    self.dataSaveFile.setMixCameraData(self.data_from_plc.mix_camera_data[0])
                    self.dataSaveFile.setModbusSensorsData(self.data_from_plc.sensors_type_list,
                                                           0,
                                                           self.data_from_plc.sensors_var_list, 'plc',
                                                            self.data_from_plc.id_list)

                    self.dataSaveFile.createFile(file_path, 'plc')
                    self.output_text.append(f"Сохранение данных из ПЛК выполнено успешно...")


                    pass
        except Exception as e:
            self.output_text.append(f"Произошло исключение: {e}")
            print(f"Произошло исключение: {e}")

    def unload_function_plc(self):

        try:
            self.driverModbusWriter = DriverModbusWriteDataPLC(int(self.id_combo.currentText().replace("Id ", "")), self.port_combo.currentText(), int(self.baudrate_combo.currentText()), 8, self.parity_combo.currentText()[:1])

            self.driverModbusWriter.sendArrayIO(self.dataPLC.getDataModbus())
            self.driverModbusWriter.writeLong(self.controllerIO.getRegBinDigit(), self.dataPLC.getBinDigital())
            self.driverModbusWriter.writeLong(self.dataPLC.reg_bit_analog_access, self.dataPLC.getBitAnalogAcess())
            self.driverModbusWriter.sendCortage(self.controllerConverter.getDataForModbus())
            self.driverModbusWriter.sendCortage(self.controllerHeat.getDataForModbus())
            self.driverModbusWriter.sendCortage(self.contollerRecup.getDataForModbus())
            self.driverModbusWriter.sendCortage(self.contollerDx.getDataForModbus())
            self.driverModbusWriter.sendCortage(self.contollerHumidifier.getDataForModbus())
            self.driverModbusWriter.sendCortage(self.controllerMixCamera.getDataForModbus())
            self.driverModbusWriter.sendArrayIO(self.contollerModbusSensors.getDataForModbus())

        except Exception:
            print("Данные в плк не выгрузились, Ошибка Modbus!!!!")
            self.output_text.append("Данные в плк не выгрузились, Ошибка Modbus!!!!")
            self.driverModbusWriter.closePort()
        else:
            print("finish")
            self.output_text.append('Выгрузка...')
            self.driverModbusWriter.closePort()

        pass

    def open_config_window(self):
        self.window_config = WindowConfig(self.config)
        self.window_config.show()

    def clear_function(self):
        self.output_text.clear()

    def get_serial_ports(self):
        """Возвращает список доступных последовательных портов."""
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports] or ['Нет доступных портов']

    def open_port(self):
        pass

    def save_config(self):
        """Сохраняет текущие настройки в файл конфигурации."""
        config = {
            'file_path_scheme_plc': self.file_button_scheme_plc.text(),
            'file_path_specification': self.file_button_specification.text(),
            'port': self.port_combo.currentText(),
            'baudrate': self.baudrate_combo.currentText(),
            'parity': self.parity_combo.currentText(),
            'id': self.id_combo.currentText()
        }

        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f)

    def load_config(self):
        """Загружает настройки из файла конфигурации."""
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                self.file_button_scheme_plc.setText(config.get('file_path_scheme_plc', 'Выбрать файл схемы плк'))
                self.file_button_specification.setText(config.get('file_path_specification', 'Выбрать файл спецификации'))
                self.port_combo.setCurrentText(config.get('port', ''))
                self.baudrate_combo.setCurrentText(config.get('baudrate', '115200'))
                self.parity_combo.setCurrentText(config.get('parity', 'None'))
                self.id_combo.setCurrentText(config.get('id', 'ID1'))

    def closeEvent(self, event):
        """Событие закрытия приложения, сохраняет конфигурацию."""
        self.save_config()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())