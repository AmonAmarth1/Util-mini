import openpyxl

class DataFileSave:
    def __init__(self):
        self.data_io_for_modbus = []
        self.data_io_var = []
        self.data_io = []

        self.converter_count_input = 0
        self.converter_count_output = 0
        self.converter_modbus_use = 0
        self.converter_type_current = 1
        self.converter_data_for_modbus = ()

        self.heat1_type = 0
        self.heat2_use = False
        self.heat2_type = 0
        self.heat_data_for_modbus = ()

        self.recup_use = False
        self.recup_type = 0
        self.recup_data_for_modbus = ()

        self.dx_use = False
        self.dx_type = 0
        self.dx_data_for_modbus = ()

        self.humidifier_use = False
        self.humidifier_data_for_modbus = ()

        self.mix_camera_use = False
        self.data_for_modbus = ()

        self.modbus_name_using_sensors = []
        self.modbus_name_type_sensors = []
        self.modbus_num_type_using_sensors = []

    def setIOData(self, io_modbus, io_var, io):
        self.data_io_for_modbus = io_modbus
        self.data_io_var = io_var
        self.data_io = io

    def setConverterData(self, count_input, count_output, modbus_use, type_current, data_modbus):
        self.converter_count_input = count_input
        self.converter_count_output = count_output
        self.converter_modbus_use = modbus_use
        self.converter_type_current = type_current
        self.converter_data_for_modbus = data_modbus

    def setHeatData(self, heat1_type, heat2_use, heat2_type, data_for_modbus):
        self.heat1_type = heat1_type
        self.heat2_use = heat2_use
        self.heat2_type = heat2_type
        self.heat_data_for_modbus = data_for_modbus

    def setRecupData(self, recup_use, recup_type, recup_data):
        self.recup_use = recup_use
        self.recup_type = recup_type
        self.recup_data_for_modbus = recup_data

    def setDxData(self, dx_use, dx_type, dx_data):
        self.dx_use = dx_use
        self.dx_type = dx_type
        self.dx_data_for_modbus = dx_data

    def setHumidifierData(self, hum_use, hum_data):
        self.humidifier_use = hum_use
        self.humidifier_data_for_modbus = hum_data

    def setMixCameraData(self, mix_use, mix_data):
        self.mix_camera_use = mix_use
        self.data_for_modbus = mix_data

    def setModbusSensorsData(self, name_sensor, type_sensor, num_type_sensor):
        self.modbus_name_using_sensors = name_sensor
        self.modbus_name_type_sensors = type_sensor
        self.modbus_num_type_using_sensors = num_type_sensor
