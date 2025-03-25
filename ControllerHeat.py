
from Literals import Literal
class ControllerHeat:
    def __init__(self):
        self.name_var_scheme = [""]

        self.heat1_type = 0

        self.heat2_use = 0
        self.heat2_type = 0

        self.heat1_type_value = list(Literal.type_heat1.values())
        self.heat2_type_value = list(Literal.type_heat2.values())

        self.reg_heat = list(Literal.reg_heat.values())

        self.data_for_modbus = ()
        pass

    def setNameVarScheme(self, var_scheme):
        self.name_var_scheme = var_scheme

    def setTypeHeat1(self):
        print(self.heat1_type_value)
        for i in range(0, len(self.name_var_scheme)):
            for j in range(0, len(self.heat1_type_value)):
                if (self.name_var_scheme[i] == self.heat1_type_value[j]):
                    self.heat1_type = j
                    return 0

    def setHeat2(self):
        print(self.heat2_type_value)
        for i in range(0, len(self.name_var_scheme)):
            if (self.name_var_scheme[i] == self.heat2_type_value[0]):
                self.heat2_use = 1
                self.heat2_type = 1
                return 0

    def getDataForModbus(self):
        self.data_for_modbus = ((self.heat1_type, self.reg_heat[0]), (self.heat2_use, self.reg_heat[1]), (self.heat2_type, self.reg_heat[2]))
        return self.data_for_modbus
