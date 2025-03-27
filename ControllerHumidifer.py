from Literals import Literal


class ControllerHumidifier:
    def __init__(self):

        self.humidifier_use = False

        self.humidifier_value = list(Literal.type_dx.values())
        self.reg_humidifier = list(Literal.reg_humidifier.values())
        self.type_reg_humidifier = list(Literal.type_reg_humidifier.values())

        self.data_for_modbus = ()
        pass

    def setNameVarScheme(self, name_var_scheme):
        self.name_var_scheme = name_var_scheme

    def setHumidifier(self):
        for i in range(0, len(self.name_var_scheme)):
            for j in range(0, len(self.humidifier_value)):
                if (self.name_var_scheme[i] == self.humidifier_value[j]):
                    self.humidifier_use = True
                    return 0

    def getDataForModbus(self):
        self.data_for_modbus = ((self.humidifier_use, self.reg_humidifier[0], self.type_reg_humidifier[0]),())
        return self.data_for_modbus

    def makeDataModbus(self, nameVarScheme):
        self.setNameVarScheme(nameVarScheme)
        self.setHumidifier()

        print(f"Humidifier use: {self.humidifier_use}")
        print(f"Humidifier data for modbus: {self.getDataForModbus()}")