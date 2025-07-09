from Literals import Literal

class Data_heat_from_gui:
    def __init__(self, config):
        self.conf = config

        self.heat1_type = 0
        self.heat1_reserve_pump = 0

        self.heat2_use = 0
        self.heat2_type = 0
        self.heat2_reserve_pump = 0

        self.reg = Literal.reg_heat
        self.reg_type = Literal.type_reg_heat

        self.modbus_data = []

    def clear(self):
        self.modbus_data.clear()

    def makeDataModbus(self):
        self.clear()

        self.modbus_data.append(((self.heat1_type, self.reg["heat1_type"], self.reg_type["heat1_type"]), ()))
        self.modbus_data.append(((self.heat1_reserve_pump, self.reg["heat1_resereve_pump"], self.reg_type["heat1_resereve_pump"]), ()))
        self.modbus_data.append(((self.heat2_use, self.reg["heat2_use"], self.reg_type["heat2_use"]), ()))
        self.modbus_data.append(((self.heat2_type, self.reg["heat2_type"], self.reg_type["heat2_type"]), ()))
        self.modbus_data.append(((self.heat2_reserve_pump, self.reg["heat2_resereve_pump"], self.reg_type["heat2_resereve_pump"]), ()))

        pass

    def getDataModbus(self):
        return self.modbus_data