from Literals import Literal

class Data_hum_from_gui:
    def __init__(self, config):
        self.conf = config

        self.hum_use = 0
        self.drainage_use = 0

        self.reg = Literal.reg_humidifier
        self.reg_type = Literal.type_reg_humidifier

        self.modbus_data = ()

    def clear(self):
        self.modbus_data = ()

    def makeDataModbus(self):
        self.clear()

        self.modbus_data = ((self.hum_use, self.reg["humidifier_use"], self.reg_type["humidifier_use"]), (self.drainage_use, self.reg["drainage_use"], self.reg_type["drainage_use"]))

        pass

    def getDataModbus(self):
        return self.modbus_data