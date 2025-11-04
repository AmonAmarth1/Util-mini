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

        self.data_io = []
        self.data_io_var = []
        self.data_io_type = []
        self.data_io_product = []
        self.data_io_min = []
        self.data_io_min_human = []
        self.data_io_max = []

        self.data_io_var_human = []
        self.data_io_type_human = []
        self.data_io_product_human = []

        self.io_product_key = list(Literal.types_product_num.keys())

        self.Ui_value = []
        self.Uo_value = []
        self.Q_value = []
        self.T_value = []
        self.analog_dig_bit = 0
        self.pwm_bit = 0

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
        self.sensor_type_single = list(Literal.sensor_type_single)
        self.sensors_data = []

        self.client = DriverModbusReadDataPLC(id, port, baud_rate, bytesize, parity)

    def get_key(self, d, value):
        for k, v in d.items():
            if v[0] == value:
                return k
    def is_bit_set(self, number, bit_position):
        # Проверяем, установлен ли бит по номеру bit_position
        return (number & (1 << bit_position)) != 0

    def binary_to_negative_decimal(self, binary_str):
        # Проверяем, что строка состоит только из 0 и 1
        if not all(bit in '01' for bit in binary_str):
            raise ValueError("Input must be a binary string.")

        # Определяем количество битов
        n = len(binary_str)

        # Если старший бит равен 1, то это отрицательное число
        if binary_str[0] == '1':
            # Вычисляем отрицательное значение
            # Инвертируем биты и добавляем 1 для получения положительного значения
            inverted_bits = ''.join('1' if bit == '0' else '0' for bit in binary_str)
            positive_value = int(inverted_bits, 2) + 1
            return -positive_value
        else:
            # Если старший бит равен 0, просто конвертируем в положительное число
            return int(binary_str, 2)

    def makeSensorsData(self):
        self.id_list = []
        self.sensors_type_list = []
        self.sensors_type_list_raw = []
        self.sensors_var_list = []
        self.sensors_var_list_raw = []
        for i in range(0, len(self.sensors_data)):
            if (self.sensors_data[i][0] == 0):
                return 0
            self.id_list.append(self.sensors_data[i][0])
            self.sensors_type_list.append(Literal.sensor_type_single[self.sensors_data[i][1]])
            self.sensors_var_list.append(self.get_key(self.Ai, self.sensors_data[i][2]))

            self.sensors_type_list_raw.append(self.sensors_data[i][1])
            self.sensors_var_list_raw.append(self.sensors_data[i][2])

    def makeIoAndVar(self):
        for i in range(0, len(self.Ui_value)):
            self.data_io.append(f"Ui{i+1}")
            self.data_io_type.append(self.Ui_value[i][1])
            self.data_io_type_human.append(Literal.types_io_input[self.Ui_value[i][1]])
            self.data_io_product.append(self.Ui_value[i][2])
            self.data_io_product_human.append(self.io_product_key[self.Ui_value[i][2]])
            if(i < 6):
                self.data_io_min_human.append(self.binary_to_negative_decimal(bin(self.Ui_value[i][3])[2:]))
                self.data_io_min.append(self.Ui_value[i][3])
                self.data_io_max.append(self.Ui_value[i][4])
            if (self.data_io_type[i] == 2):
                self.data_io_var_human.append(self.get_key(self.Di, self.Ui_value[i][0]))
                self.data_io_var.append(self.Ui_value[i][0])
            else:
                self.data_io_var_human.append(self.get_key(self.Ai, self.Ui_value[i][0]))
                self.data_io_var.append(self.Ui_value[i][0])
        for i in range(0, len(self.Uo_value)):
            self.data_io_type.append(self.Uo_value[i][1])
            self.data_io_type_human.append(Literal.types_io_output_2[self.Uo_value[i][1]])
            self.data_io.append(f"Uo{i+1}")
            if (self.is_bit_set(self.analog_dig_bit, i)):
                self.data_io_var_human.append(self.get_key(self.Do, self.Uo_value[i][0]))
                self.data_io_var.append(self.Uo_value[i][0])
            else:
                self.data_io_var_human.append(self.get_key(self.Ao, self.Uo_value[i][0]))
                self.data_io_var.append(self.Uo_value[i][0])
        for i in range(0, len(self.Q_value)):
            self.data_io.append(f"Q{i + 1}")
            key = self.get_key(self.Do, self.Q_value[i][0])
            if (key != None):
                self.data_io_var_human.append(key)
                self.data_io_var.append(self.Q_value[i][0])
            else:
                self.data_io_var_human.append('-')
                self.data_io_var.append(self.Q_value[i][0])
        for i in range(0, len(self.T_value)):
            self.data_io.append(f"T{i + 1}")
            self.data_io_var_human.append(self.get_key(self.Do, self.T_value[i][0]))
            self.data_io_var.append(self.T_value[i][0])

    def readAllData(self):
        self.readIO()
        self.readConverter()
        self.readHeat()
        self.readRecup()
        self.readDx()
        self.readHumidifier()
        self.readMixCamera()
        self.readSensors()
        self.makeIoAndVar()
        self.makeSensorsData()

    def readIO(self):
        reg_analog_digit = 0
        reg_pwm = 0
        for i in range(0, len(self.RegUi)):
            reg = self.RegUi[f"UI{i + 1}"]
            if (reg != None):
                self.Ui_value.append(self.client.readCortageIO(reg))
        for i in range(0, 8):
            reg1 = self.RegUo[f"UO{i + 1}"]
            if (reg1 != None):
                self.Uo_value.append(self.client.readCortageIO((reg1[0], reg1[1], reg1[2])))
                reg_analog_digit = reg1[3]
                reg_pwm = reg1[4]
        for i in range(0, 5):
            reg2 = self.RegUo[f"Q{i + 1}"]
            if (reg2 != None):
                self.Q_value.append(self.client.readCortageIO((reg2[0], reg2[1], reg2[2])))
        for i in range(0, 2):
            reg3 = self.RegUo[f"T{i + 1}"]
            if (reg3 != None):
                self.T_value.append(self.client.readCortageIO((reg3[0], reg3[1], reg3[2])))

        self.analog_dig_bit = self.client.readSingleLong(reg_analog_digit)
        self.pwm_bit = self.client.readSingleLong(reg_pwm)

    def readConverter(self):
        for i in range(0, len(self.converter_list_reg)):
            self.converter_data.append(self.client.readData(self.converter_list_reg[i], self.converter_type_list_reg[i]))
        self.converter_type = Literal.types_converter_num[self.converter_data[4]]
    def readHeat(self):
        for i in range(0, len(self.reg_heat)):
            self.heat_data.append(self.client.readData(self.reg_heat[i], self.type_reg_heat[i]))
        self.type_heat1 = Literal.type_heat_num[self.heat_data[0]]
        self.type_heat2 = Literal.type_heat_num[self.heat_data[2]]

    def readRecup(self):
        for i in range(0, len(self.reg_recup)):
            self.recup_data.append(self.client.readData(self.reg_recup[i], self.type_reg_recup[i]))
        self.recup_type = Literal.type_recup_num[self.converter_data[1]]

    def readDx(self):
        for i in range(0, len(self.reg_dx)):
            self.dx_data.append(self.client.readData(self.reg_dx[i], self.type_reg_dx[i]))
        self.type_dx = Literal.type_dx_num[self.dx_data[1]]
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
            if (sensor1[0] == 0):
                break
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

        print("Данные по входам человеческие:")
        print(self.data_io)
        print(self.data_io_var_human)
        print(self.data_io_type_human)
        print(self.data_io_product_human)
        print(self.data_io_min)
        print(self.data_io_max)

        print("Данные по modbus sensors:")
        print(self.id_list)
        print(self.sensors_type_list)
        print(self.sensors_var_list)
        self.client.closePort()