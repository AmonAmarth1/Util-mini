from Literals import Literal

class Data_sensors_from_gui:
    def __init__(self, config):
        self.conf = config

        self.id = []
        self.type = []
        self.var = []

        self.reg = Literal.reg_modbus_sensor
        self.reg_type = Literal.type_reg_modbus_sensor

        self.sensors_use_bit = 0
        self.analog_bit_access_io = 0
        self.analog_bit_access = 0
        self.sensors_use = 0

        self.modbus_data = []

    def clear(self):
        self.analog_bit_access = 0
        self.sensors_use = 0
        self.id.clear()
        self.type.clear()
        self.var.clear()
        self.modbus_data.clear()

    def setAnalogUseBit(self):
        for i in range(0, len(self.var)):
            if self.id[i] != 0:
                if self.var[i] != 0:
                    self.sensors_use = 1
                    self.analog_bit_access = self.analog_bit_access | (1 << self.var[i])
                    self.sensors_use_bit = self.sensors_use_bit | (1 << self.var[i])
        self.analog_bit_access = self.analog_bit_access | self.analog_bit_access_io
        print(f'Analog bit use: {self.analog_bit_access}!')

    def makeDataModbus(self):


        self.setAnalogUseBit()

        for i in range(0, len(self.id)):

            self.modbus_data.append(((self.id[i], self.reg["id_sensor_1"] + i, self.reg_type["id_sensor_1"]), ()))
            self.modbus_data.append(((self.type[i], self.reg["type_sensor_1"] + i, self.reg_type["type_sensor_1"]), ()))
            self.modbus_data.append(((self.var[i], self.reg["type_var_sensor_1"] + i, self.reg_type["type_var_sensor_1"]), ()))

        self.modbus_data.append(((self.sensors_use, self.reg["modbus_sensors_use"], self.reg_type["modbus_sensors_use"]), ()))
        self.modbus_data.append(((self.sensors_use_bit, self.reg["sensors_use_bit"], self.reg_type["sensors_use_bit"]), ()))
        self.modbus_data.append(
            ((self.analog_bit_access, Literal.reg_analog_var_access, Literal.WRITE_LONG), ()))

    def getDataModbus(self):
        return self.modbus_data