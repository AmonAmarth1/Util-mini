from Literals import Literal

from DriverModbusReadDataPLC import DriverModbusReadDataPLC

class DataFromPLC:

    def __init__(self, config, id, port, baud_rate, bytesize, parity):
        self.RegUi = config.RegUi
        self.RegUo = config.RegUo

        self.Ai = config.Ai
        self.Di = config.Di
        self.Ao = config.Ao
        self.Do = config.Do
        self.Method = config.Method

        self.Ui_value = []
        self.Uo_value = []
        self.Q_value = []
        self.T_value = []

        self.converter_list_reg = list(Literal.register_converter.values())
        self.converter_type_list_reg = list(Literal.type_reg_converter.values())
        self.converter_data = []

        self.reg_heat = list(Literal.reg_heat.values())
        self.type_reg_heat = list(Literal.type_reg_heat.values())
        self.heat_data = []

        self.reg_recup = list(Literal.reg_recup.values())
        self.type_reg_recup = list(Literal.type_reg_recup.values())
        self.recup_data = []

        self.reg_dx = list(Literal.reg_dx.values())
        self.type_reg_dx = list(Literal.type_reg_dx.values())
        self.dx_data = []

        self.reg_humidifier = list(Literal.reg_humidifier.values())
        self.type_reg_humidifier = list(Literal.type_reg_humidifier.values())
        self.humidifier_data = []

        self.reg_mix_camera = list(Literal.reg_mix_camera.values())
        self.type_reg_mix_camera = list(Literal.type_reg_mix_camera.values())
        self.mix_camera_data = []

        self.reg_sensor = list(Literal.reg_modbus_sensor.values())
        self.type_reg_sensor = list(Literal.type_reg_modbus_sensor.values())
        self.sensors_data = []

        self.client = DriverModbusReadDataPLC(id, port, baud_rate, bytesize, parity)

    def readAllData(self):
        self.readIO()
        self.readConverter()
        self.readHeat()
        self.readRecup()
        self.readDx()
        self.readHumidifier()
        self.readMixCamera()
        self.readSensors()
    def readIO(self):
        for i in range(0, len(self.RegUi)):
            reg = self.RegUi[f"UI{i + 1}"]
            if (reg != None):
                self.Ui_value.append(self.client.readCortageIO(reg))
        for i in range(0, 8):
            reg1 = self.RegUo[f"UO{i + 1}"]
            if (reg1 != None):
                self.Uo_value.append(self.client.readCortageIO((reg1[0], reg1[1], reg1[2])))
        for i in range(0, 5):
            reg2 = self.RegUo[f"Q{i + 1}"]
            if (reg2 != None):
                self.Q_value.append(self.client.readCortageIO((reg2[0], reg2[1], reg2[2])))
        for i in range(0, 2):
            reg3 = self.RegUo[f"T{i + 1}"]
            if (reg3 != None):
                self.T_value.append(self.client.readCortageIO((reg3[0], reg3[1], reg3[2])))

    def readConverter(self):
        for i in range(0, len(self.converter_list_reg)):
            self.converter_data.append(self.client.readData(self.converter_list_reg[i], self.converter_type_list_reg[i]))

    def readHeat(self):
        for i in range(0, len(self.reg_heat)):
            self.heat_data.append(self.client.readData(self.reg_heat[i], self.type_reg_heat[i]))

    def readRecup(self):
        for i in range(0, len(self.reg_recup)):
            self.recup_data.append(self.client.readData(self.reg_recup[i], self.type_reg_recup[i]))

    def readDx(self):
        for i in range(0, len(self.reg_dx)):
            self.dx_data.append(self.client.readData(self.reg_dx[i], self.type_reg_dx[i]))
    def readHumidifier(self):
        for i in range(0, len(self.reg_humidifier)):
            self.humidifier_data.append(self.client.readData(self.reg_humidifier[i], self.type_reg_humidifier[i]))
    def readMixCamera(self):
        for i in range(0, len(self.reg_mix_camera)):
            self.mix_camera_data.append(self.client.readData(self.reg_mix_camera[i], self.type_reg_mix_camera[i]))
        pass

    def readSensors(self):
        for i in range(0, 32):
            sensor1 = []
            for j in range(0, len(self.reg_sensor) - 2):
                sensor1.append(self.client.readData(self.reg_sensor[j] + i, self.type_reg_sensor[j]))
            self.sensors_data.append(sensor1)

    def print(self):
        print("Данные по входам, выходам ПЛК:")
        print(self.Ui_value)
        print(self.Uo_value)
        print(self.Q_value)
        print(self.T_value)

        print("Данные с ПЧ:")
        print(self.converter_data)

        print("Данные с нагревателя:")
        print(self.heat_data)

        print("Данные с рекуператора:")
        print(self.recup_data)

        print("Данные с охладителя:")
        print(self.dx_data)

        print("Данные с увлажнителя:")
        print(self.humidifier_data)

        print("Данные с камеры смешения:")
        print(self.mix_camera_data)

        print("Данные c modbus датчиков:")
        for i in range(0, len(self.sensors_data)):
            print(self.sensors_data[i])
