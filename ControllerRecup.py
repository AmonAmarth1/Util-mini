from Literals import Literal

class ControllerRecup:
    def __init__(self):

        self.recup_use = False
        self.recup_type = 0
        self.recup_type_name = ""

        self.recup_type_value = list(Literal.type_recup.values())
        self.recup_type_key = list(Literal.type_recup.keys())
        self.reg_recup = list(Literal.reg_recup.values())
        self.type_reg_recup = list(Literal.type_reg_recup.values())

        self.data_for_modbus = ()
        pass


    def setNameVarScheme(self, var_scheme):
        self.name_var_scheme = var_scheme

    def setTypeRecup(self):
        for i in range(0, len(self.name_var_scheme)):
            for j in range(0, len(self.recup_type_value)):
                if (self.name_var_scheme[i] == self.recup_type_value[j]):
                    self.recup_use = True
                    self.recup_type = j + 1
                    self.recup_type_name = self.recup_type_key[j]
                    return 0

    def getDataForModbus(self):
        self.data_for_modbus = ((self.recup_use, self.reg_recup[0], self.type_reg_recup[0]), (self.recup_type, self.reg_recup[1], self.type_reg_recup[1]))
        return self.data_for_modbus

    def makeDataModbus(self, nameVarScheme):
        self.setNameVarScheme(nameVarScheme)
        self.setTypeRecup()

        print(f"recup type: {self.recup_type}")
        print(f"recup data for modbus: {self.getDataForModbus()}")