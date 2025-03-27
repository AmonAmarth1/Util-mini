from Literals import Literal

class ControllerDx:
    def __init__(self):

        self.dx_use = False
        self.dx_type = 0

        self.dx_type_value = list(Literal.type_dx.values())
        self.reg_dx = list(Literal.reg_dx.values())
        self.type_reg_dx = list(Literal.type_reg_dx.values())

        self.data_for_modbus = ()
        pass

    def setNameVarScheme(self, var_scheme):
        self.name_var_scheme = var_scheme

    def setDx(self):
        for i in range(0, len(self.name_var_scheme)):
            for j in range(0, len(self.dx_type_value)):
                if (self.name_var_scheme[i] == self.dx_type_value[j]):
                    self.dx_use = True
                    self.dx_type = 1
                    return 0

    def getDataForModbus(self):
        self.data_for_modbus = ((self.dx_use, self.reg_dx[0], self.type_reg_dx[0]), (self.dx_type, self.reg_dx[1], self.type_reg_dx[1]))
        return self.data_for_modbus

    def makeDataModbus(self, nameVarScheme):
        self.setNameVarScheme(nameVarScheme)
        self.setDx()

        print(f"Dx type: {self.dx_type}")
        print(f"Dx data for modbus: {self.getDataForModbus()}")