from Literals import Literal

class Data_vent_from_gui:
    def __init__(self, config):
        self.conf = config

        self.vent_in_num = 0
        self.vent_out_num = 0

        self.vent_in_modbus_use = 0
        self.vent_out_modbus_use = 0

        self.vent_in_type = 2
        self.vent_out_type = 2

        self.vent_in_id = 0
        self.vent_out_id = 10

        self.vent_in_reserve = 0
        self.vent_out_reserve = 0

        self.reg = Literal.register_converter
        self.type_reg = Literal.type_reg_converter

        self.modbus_data = []

    def clear(self):
        self.modbus_data.clear()

    def makeDataModebus(self):
        self.clear()
        self.modbus_data.append(((self.vent_in_num, self.reg["input_count"], self.type_reg["input_count"]), ()))
        self.modbus_data.append(((self.vent_out_num, self.reg["output_count"], self.type_reg["output_count"]), ()))

        self.modbus_data.append(((self.vent_in_modbus_use, self.reg["input_converter_modbus_use"], self.type_reg["input_converter_modbus_use"]), ()))
        self.modbus_data.append(((self.vent_out_modbus_use, self.reg["output_converter_modbus_use"], self.type_reg["output_converter_modbus_use"]), ()))

        self.modbus_data.append(((self.vent_in_type, self.reg["input_type"],
                                  self.type_reg["input_type"]), ()))
        self.modbus_data.append(((self.vent_out_type, self.reg["output_type"],
                                  self.type_reg["output_type"]), ()))

        self.modbus_data.append(((self.vent_in_id, self.reg["input_adres_1"],
                                  self.type_reg["input_adres_1"]), ()))
        self.modbus_data.append(((self.vent_out_id, self.reg["output_adres_1"],
                                  self.type_reg["output_adres_1"]), ()))

        self.modbus_data.append(((self.vent_in_reserve, self.reg["input_type_reserve"],
                                  self.type_reg["input_type_reserve"]), ()))
        self.modbus_data.append(((self.vent_out_reserve, self.reg["output_type_reserve"],
                                  self.type_reg["output_type_reserve"]), ()))

    def getDataModbus(self):
        return self.modbus_data






        