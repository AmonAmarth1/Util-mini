
from Literals import Literal
class ControllerConverter:
    def __init__(self):
        self.name_var_scheme = [""]
        self.name_var_specification = [""]
        self.product_number = [""]

        self.count_converter_input = 0
        self.count_converter_output = 0

        self.modbus_use = 0
        self.type_current_converter = 1

        self.list_type_converter_keys = list(Literal.types_converter.keys())
        self.list_type_converter_values = list(Literal.types_converter.values())

        self.list_reg = list(Literal.register_converter.values())

        self.data_for_modbus = ()

    def setNameVarScheme(self, name):
        self.name_var_scheme = name

    def setNameVarSpecification(self, name):
        self.name_var_specification = name

    def setProductName(self, product):
        self.product_number = product

    def countInputConverter(self):
        for i in range(0, len(self.name_var_specification)):
            if (self.name_var_specification[i].find("1U") != -1):
                self.count_converter_input = self.count_converter_input + 1
        return self.count_converter_input

    def countOutputConverter(self):
        for i in range(0, len(self.name_var_specification)):
            if (self.name_var_specification[i].find("2U") != -1):
                self.count_converter_output = self.count_converter_output + 1
        return self.count_converter_output

    def checkModbusUse(self):
        if(self.count_converter_input > 2 or self.count_converter_output > 2):
            self.modbus_use = 1
            return self.modbus_use
        else:
            for i in range(0, len(self.name_var_scheme)):
                if(self.name_var_scheme[i].find("1U") != -1):
                    self.modbus_use = 0
                    return self.modbus_use
            self.modbus_use = 1
        return self.modbus_use

    def checkTypeConverter(self):
        for i in range(0, len(self.product_number)):
            for j in range(0, len(self.list_type_converter_keys)):
                if (self.product_number[i].find(f"{self.list_type_converter_keys[j]}") != -1):
                    self.type_current_converter = self.list_type_converter_values[j]
                    return 0
        return 0

    def makeDataForModbus(self):
        self.data_for_modbus = ((self.modbus_use, self.list_reg[0]), (self.modbus_use, self.list_reg[1]), (self.count_converter_input, self.list_reg[2]), (self.count_converter_output, self.list_reg[3]), (self.type_current_converter, self.list_reg[4]), (self.type_current_converter, self.list_reg[5]))
    def getCountInputConverter(self):
        return self.count_converter_input

    def getCountOutputConverter(self):
        return self.count_converter_output

    def getModbusUse(self):
        return self.modbus_use

    def getTypeCurrecntConverter(self):
        return self.type_current_converter

    def getDataForModbus(self):
        return self.data_for_modbus