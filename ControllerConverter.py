
from Literals import Literal
class ControllerConverter:
    def __init__(self):
        self.name_var_scheme = [""]
        self.name_var_specification = [""]
        self.product_number = [""]

        self.count_converter_input = 0
        self.count_converter_output = 0

        self.modbus_use = 0
        self.type_current_converter = 2

        self.list_type_converter_keys = list(Literal.types_converter.keys())
        self.list_type_converter_values = list(Literal.types_converter.values())

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

    def getCountInputConverter(self):
        return self.count_converter_input

    def getCountOutputConverter(self):
        return self.count_converter_output

    def getModbusUse(self):
        return self.modbus_use