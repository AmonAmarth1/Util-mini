from Literals import Literal

class Data_io_from_gui:
    def __init__(self, config):
        self.conf = config

        self.var = []
        self.type = []
        self.method = []
        self.min = []
        self.max = []

        self.analog_bit_access = 0

        self.Q_var = []
        self.T_var = []

        self.U_var = []
        self.U_type = []
        self.U_period = []
        self.digit_bit = Literal.DEFAULT_BIN_OUTPUT_DIGIT
        self.pwm_bit = 0

        self.data_for_modbus = []

    def clear(self):
        self.var.clear()
        self.type.clear()
        self.method.clear()
        self.min.clear()
        self.max.clear()
        self.analog_bit_access = 0

        self.Q_var.clear()
        self.T_var.clear()

        self.U_var.clear()
        self.U_type.clear()
        self.U_period.clear()
        self.digit_bit = Literal.DEFAULT_BIN_OUTPUT_DIGIT

        self.data_for_modbus.clear()

    def setAnalogUseBit(self):
        for i in range(0, len(self.var)):
            if self.type[i] != 2:
                if self.var[i] != 0:
                    self.analog_bit_access = self.analog_bit_access | (1 << self.var[i])
        print(f'Analog bit use: {self.analog_bit_access}!')

    def setDigitUseBit(self):
        for i in range(0, 8):
            if self.U_type[i] == 17:
                self.digit_bit = self.digit_bit | (1 << i)
            if self.U_type[i] == 18 and self.U_period[i] != 0:
                self.pwm_bit = self.pwm_bit | (1 << i)

    def makeDataIOModbus(self):
        for i in range(0, 18):
            reg = self.conf.RegUi[f"UI{i + 1}"]
            if i < 6:
                self.data_for_modbus.append(((self.var[i], reg[0]), (self.type[i], reg[1]), (self.method[i], reg[2]), (self.min[i], reg[3]), (self.max[i], reg[4])))
            else:
                self.data_for_modbus.append(((self.var[i], reg[0]), (self.type[i], reg[1]), (self.method[i], reg[2])))
        tuple_analog_use = ((self.analog_bit_access, Literal.reg_analog_var_access, Literal.WRITE_LONG),())
        self.data_for_modbus.append(tuple_analog_use)

        for i in range(0, 8):
            reg = self.conf.RegUo[f"UO{i + 1}"]
            self.data_for_modbus.append(((self.U_var[i], reg[0]), (self.U_type[i], reg[1]), (self.U_period[i], reg[2])))
        tuple_digit_use = ((self.digit_bit, Literal.reg_bin_digit, Literal.WRITE_LONG), ())
        self.data_for_modbus.append(tuple_digit_use)
        tuple_pwm_use = ((self.pwm_bit, Literal.pwm_out), ())
        self.data_for_modbus.append(tuple_pwm_use)

        for i in range(0, 5):
            reg = self.conf.RegUo[f"Q{i + 1}"]
            self.data_for_modbus.append(((self.Q_var[i], reg[0]), ()))

        for i in range(0, 2):
            reg = self.conf.RegUo[f"T{i + 1}"]
            self.data_for_modbus.append(((self.T_var[i], reg[0]), ()))

    def getDataModbus(self):
        return self.data_for_modbus