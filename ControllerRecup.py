from Literals import Literal

class ControllerRecup:
    def __init__(self):
        self.name_var_scheme = [""]

        self.recup_use = 0
        self.recup_type = 0

        self.recup_type_value = list(Literal.type_recup.values())
        self.reg_recup = list(Literal.reg_recup.values())

        self.data_for_modbus = ()
        pass

    def setNameVarScheme(self, var_scheme):
        self.name_var_scheme = var_scheme

    def setTypeRecup(self):
        for i in range(0, len(self.name_var_scheme)):
            for j in range(0, len(self.recup_type_value)):
                if (self.name_var_scheme[i] == self.recup_type_value[j]):
                    self.recup_use = 1
                    self.recup_type = j + 1
                    return 0

    def getDataForModbus(self):
        self.data_for_modbus = ((self.recup_use, self.reg_recup[0]), (self.recup_type, self.reg_recup[1]))
        return self.data_for_modbus