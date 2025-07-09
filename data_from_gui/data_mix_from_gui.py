from Literals import Literal

class Data_mix_from_gui:
    def __init__(self, config):
        self.conf = config

        self.mix_use = 0

        self.reg = Literal.reg_mix_camera
        self.reg_type = Literal.type_reg_mix_camera

        self.modbus_data = ()

    def clear(self):
        self.modbus_data = ()

    def makeDataModbus(self):
        self.clear()

        self.modbus_data = ((self.mix_use, self.reg["mix_camera_use"], self.reg_type["mix_camera_use"]), ())

        pass

    def getDataModbus(self):
        return self.modbus_data