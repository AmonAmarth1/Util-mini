from Literals import Literal

class ControllerIO:
    def __init__(self, config):
        self.conf = config
        self.regBinDigit = 0
        self.analog_bit_access = 0

    def getGroupTypeio(self, var_eplan):
        group_typeio = ""
        if f"{var_eplan}" in self.conf.typeio:
            group_typeio = self.conf.typeio[f"{var_eplan}"]
        return  group_typeio

    def getNameVarPlC(self, var_eplan):
        var_plc = ""
        if f"{var_eplan}" in self.conf.Var:
            var_plc = self.conf.Var[f"{var_eplan}"]
        else:
            print("key not exist!!!!")
        return var_plc

    def getNumVar(self, group_typeio, var_plc):
        num = 0
        var_dict = getattr(self.conf, group_typeio)

        if f"{var_plc}" in var_dict:
            num = var_dict[f"{var_plc}"][0]
        if (group_typeio == "Ai"):
            self.analog_bit_access = self.analog_bit_access | pow(2, num)
        return num

    def getNumTypeIO(self, group_typeio, type_io):
        num_type = Literal.types_key_io[group_typeio]
        return num_type

    def getNumMethodIO(self, group_type_io, product_num_io, var_eplan, use_specification):
        if (use_specification == 0):
            if f"{var_eplan}" in self.conf.Method:
                method = self.conf.Method[f"{var_eplan}"][0]
                return method
        else:
            if (group_type_io == "Ao" or group_type_io == "Do"):
                return 1000
            key_product = list(Literal.types_product_num.keys())
            value_product = list(Literal.types_product_num.values())

            if(product_num_io != None):
                for i in range(0, len(key_product)):
                    if (product_num_io.find(key_product[i]) != -1):
                        method = value_product[i]
                        return method
        return None

    def getBinOutputDigit(self, io):

        types_key = Literal.types_key_UO
        new_bin_num = ''
        if f"{io}" in types_key:
            new_bin_num = types_key[f"{io}"]
            print(f"new bin: {new_bin_num}")
        return new_bin_num

    def checkUseUniversalOutput(self, io):
        for i in range(1, Literal.NUMBER_UNIVERSAL_OUTPUT + 1):
            if (io == f"UO{i}"):
                print("universal output use!")
                return 1
        return 0
    def getRegBinDigit(self):
        return self.regBinDigit

    def getRegistr(self, group_typeio, name_io):
        reg = (0, 0, 0)
        if (group_typeio == "Ai" or group_typeio == "Di"):
            if f"{name_io}" in self.conf.RegUi:
                reg = self.conf.RegUi[f"{name_io}"]

        if (group_typeio == "Ao" or group_typeio == "Do"):
            if f"{name_io}" in self.conf.RegUo:
                reg = self.conf.RegUo[f"{name_io}"]
                self.regBinDigit = self.conf.RegUo[f"{name_io}"][Literal.POSITION_REG_BIN_DIGIT]
        return reg

    def getValueAndReg(self, var_eplan, io, product_num_io):
        val_reg = (0, 0, 0, 0, 0, 0)

        var_plc = self.getNameVarPlC(var_eplan)
        group_typeio = self.getGroupTypeio(var_eplan)

        print(f"group_typeio: {group_typeio}")
        print(f"var_plc: {var_plc}")

        if (var_plc == ""):
            return None
        num_var_plc = self.getNumVar(group_typeio[0], var_plc[0])
        print(f"num_var_plc: {num_var_plc}")

        num_typeio = self.getNumTypeIO(group_typeio[0], 0)
        print(f"num_typeio: {num_typeio}")

        num_method = self.getNumMethodIO(group_typeio[0], product_num_io, var_eplan, 0)
        print(f"num_method: {num_method}")

        reg = self.getRegistr(group_typeio[0], io)
        print(reg)

        use_universal_output = self.checkUseUniversalOutput(io)
        bin_output_digit = Literal.DEFAULT_BIN_OUTPUT_DIGIT

        if (group_typeio[0] == "Do" and use_universal_output == 1):
            bin_output_digit = self.getBinOutputDigit(io)

        if (group_typeio[0] == "Ai" or group_typeio[0] == "Di"):
            val_reg = ((num_var_plc, reg[0]), (num_typeio, reg[1]), (num_method, reg[2]))
        else:
            val_reg = ((num_var_plc, reg[0]), (num_typeio, reg[1]), (num_method, reg[2]), (bin_output_digit, reg[3]))

        return val_reg
