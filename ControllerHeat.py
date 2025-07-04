
from Literals import Literal
class ControllerHeat:
    def __init__(self):
        self.name_var_scheme = [""]

        self.heat1_type = 0
        self.heat1_type_name = ""

        self.heat2_use = False
        self.heat2_type = 0
        self.heat2_type_name = ""

        self.heat1_type_value = list(Literal.type_heat1.values())
        self.heat1_type_key = list(Literal.type_heat1.keys())
        self.heat2_type_value = list(Literal.type_heat2.values())
        self.heat2_type_key = list(Literal.type_heat2.keys())

        self.reg_heat = list(Literal.reg_heat.values())
        self.type_reg_heat = list(Literal.type_reg_heat.values())

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
                    self.heat1_type_name = self.heat1_type_key[j]
                    return 0

    def setHeat2(self):
        print(self.heat2_type_value)
        for i in range(0, len(self.name_var_scheme)):
            if (self.name_var_scheme[i] == self.heat2_type_value[0]):
                self.heat2_use = True
                self.heat2_type = 1
                self.heat2_type_name = self.heat2_type_key[0]
                return 0

    def getDataForModbus(self):
        self.data_for_modbus = ((self.heat1_type, self.reg_heat[0], self.type_reg_heat[0]), (self.heat2_use, self.reg_heat[1], self.type_reg_heat[1]), (self.heat2_type, self.reg_heat[2], self.type_reg_heat[2]))
        return self.data_for_modbus

    def makeDataModbus(self, NameVarScheme):
        self.setNameVarScheme(NameVarScheme)
        self.setTypeHeat1()
        self.setHeat2()

        print(f"heat1 type: {self.heat1_type}")
        print(f"heat2 use: {self.heat2_use}")
        print(f"heat2 type: {self.heat2_type}")
        print(f"heat for modbus: {self.getDataForModbus()}")