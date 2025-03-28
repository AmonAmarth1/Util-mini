from Literals import Literal


class ControllerMixCamera:
    def __init__(self):

        self.mix_camera_use = False

        self.mix_camera_value = list(Literal.mix_camera.values())
        self.reg_mix_camera = list(Literal.reg_mix_camera.values())
        self.type_reg_mix_camera = list(Literal.type_reg_mix_camera.values())

        self.data_for_modbus = ()
        pass

    def setNameVarScheme(self, name_var_scheme):
        self.name_var_scheme = name_var_scheme

    def setMixCamera(self):
        for i in range(0, len(self.name_var_scheme)):
            for j in range(0, len(self.mix_camera_value)):
                if (self.name_var_scheme[i] == self.mix_camera_value[j]):
                    self.mix_camera_use = True
                    return 0

    def getDataForModbus(self):
        self.data_for_modbus = ((self.mix_camera_use, self.reg_mix_camera[0], self.type_reg_mix_camera[0]),())
        return self.data_for_modbus

    def makeDataModbus(self, nameVarScheme):
        self.setNameVarScheme(nameVarScheme)
        self.setMixCamera()

        print(f"Mix camera use: {self.mix_camera_use}")
        print(f"Mix camera data for modbus: {self.getDataForModbus()}")