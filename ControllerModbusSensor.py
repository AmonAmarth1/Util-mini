from Literals import Literal


class ControllerModbusSensor:
    def __init__(self):

        self.modbus_sensors_use = 0
        self.count_modbus_sensor = 0
        self.id_1 = 20
        self.name_using_sensors = []
        self.name_type_sensors = []
        self.num_type_using_sensors = []

        self.sensor_name_key = list(Literal.sensor_name_num.keys())
        self.sensor_name_num = Literal.sensor_name_num

        self.reg_sensor = list(Literal.reg_modbus_sensor.values())
        self.type_reg_sensor = list(Literal.type_reg_modbus_sensor.values())

        self.sensor_type_key = list(Literal.sensor_type.keys())
        self.sensor_type_value = list(Literal.sensor_type.values())

        self.data_for_modbus = []
        pass

    def setNameVarSchemeAndProductNumber(self, name_var_specification, product_number):
        self.name_var_specification = name_var_specification
        self.product_number = product_number

    def setModbusSensors(self):
        for i in range(0, len(self.name_var_specification)):
            for j in range(0, len(self.sensor_name_key)):
                if (self.name_var_specification[i] == self.sensor_name_key[j]):
                    self.count_modbus_sensor = self.count_modbus_sensor + 1
                    self.modbus_sensors_use = 1
                    self.name_using_sensors.append(self.sensor_name_key[j])
                    for m in range(i, len(self.product_number)):
                        for k in range(0, len(self.sensor_type_key)):
                            if (self.product_number[m].find(f"{self.sensor_type_key[k]}") != -1):
                                self.name_type_sensors.append(self.sensor_type_key[k])
                                self.num_type_using_sensors.append(self.sensor_type_value[k])
                                pass


    def makeDataForModbus(self):
        count = 0
        for i in range(0, self.count_modbus_sensor):
            name = self.name_using_sensors[i]
            if (self.modbus_sensors_use == 1):
                self.data_for_modbus.append(((self.modbus_sensors_use, self.reg_sensor[3], self.type_reg_sensor[3]), (self.modbus_sensors_use, self.reg_sensor[4], self.type_reg_sensor[4])))
            if (len(self.sensor_name_num[name]) == 1):
                self.data_for_modbus.append(((self.id_1, self.reg_sensor[0] + count, self.type_reg_sensor[0]), (self.num_type_using_sensors[i][0], self.reg_sensor[1] + count, self.type_reg_sensor[1]), (self.sensor_name_num[name][0], self.reg_sensor[2] + count, self.type_reg_sensor[2])))
                count = count + 1
            if (len(self.sensor_name_num[name]) == 2):
                self.data_for_modbus.append(((self.id_1, self.reg_sensor[0] + count, self.type_reg_sensor[0]), (self.num_type_using_sensors[i][0], self.reg_sensor[1] + count, self.type_reg_sensor[1]), (self.sensor_name_num[name][0], self.reg_sensor[2] + count, self.type_reg_sensor[2]),
                                             (self.id_1, self.reg_sensor[0] + count + 1, self.type_reg_sensor[0]), (self.num_type_using_sensors[i][1], self.reg_sensor[1] + count + 1, self.type_reg_sensor[1]), (self.sensor_name_num[name][1], self.reg_sensor[2] + count + 1, self.type_reg_sensor[2])))
                count = count + 2
            self.id_1 = self.id_1 + 1


    def getDataForModbus(self):
        return self.data_for_modbus
