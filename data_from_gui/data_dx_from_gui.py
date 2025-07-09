from Literals import Literal

class Data_dx_from_gui:
    def __init__(self, config):
        self.conf = config

        self.dx_use = 0
        self.dx_type = 0
        self.dx_heat_use = 0

        self.reg = Literal.reg_dx
        self.reg_type = Literal.type_reg_dx

        self.modbus_data = []

    def clear(self):
        self.modbus_data.clear()

    def makeDataModbus(self):
        self.clear()

        self.modbus_data.append(((self.dx_use, self.reg["use_dx"], self.reg_type["use_dx"]), ()))
        self.modbus_data.append(((self.dx_type, self.reg["config_dx"], self.reg_type["config_dx"]), ()))
        self.modbus_data.append(((self.dx_heat_use, self.reg["heat_dx"], self.reg_type["heat_dx"]), ()))

        pass

    def getDataModbus(self):
        return self.modbus_data