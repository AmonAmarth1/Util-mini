from Literals import Literal

class Data_recup_from_gui:
    def __init__(self, config):
        self.conf = config

        self.recup_use = 0
        self.type = 0
        self.modbus_use = 0
        self.id = 0
        self.recup_rpm = 0
        self.type_conv = 0

        self.reg = Literal.reg_recup
        self.reg_type = Literal.type_reg_recup

        self.modbus_data = []

    def clear(self):
        self.modbus_data.clear()

    def makeDataModbus(self):

        self.clear()

        self.modbus_data.append(((self.recup_use, self.reg["use_recup"], self.reg_type["use_recup"]), ()))
        self.modbus_data.append(((self.type, self.reg["type_recup"], self.reg_type["type_recup"]), ()))
        self.modbus_data.append(((self.modbus_use, self.reg["activate_modbus"], self.reg_type["activate_modbus"]), ()))
        self.modbus_data.append(((self.id, self.reg["id"], self.reg_type["id"]), ()))
        self.modbus_data.append(((self.recup_rpm, self.reg["nominal_rpm"], self.reg_type["nominal_rpm"]), ()))
        self.modbus_data.append(((self.type_conv, self.reg["type_conv"], self.reg_type["type_conv"]), ()))

        pass

    def getDataModbus(self):
        return self.modbus_data