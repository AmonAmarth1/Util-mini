
import openpyxl

class DataFromEplan:

    def __init__(self):
        self.io = {0: ""}
        self.name_var = {0: ""}
        self.file1_length = 0

        self.io.clear()
        self.name_var.clear()

        self.name_var_1 = {0: ""}
        self.product_number = {0: ""}
        self.file2_length = 0

        self.name_var_1.clear()
        self.product_number.clear()



    def readExel_scheme_plc(self, file_path_scheme_plc):

        wb = openpyxl.load_workbook(file_path_scheme_plc)
        sheet = wb['Схема ПЛК']

        for i in range(1, sheet.max_row):
            io = sheet[f"A{i}"]
            name_var = sheet[f"B{i}"]
            if (name_var.value != None):
                self.name_var[self.file1_length] = name_var.value
                self.io[self.file1_length] = io.value
                self.file1_length = self.file1_length + 1


    def readExel_specification(self, file_path_specification):

        wb = openpyxl.load_workbook(file_path_specification)
        sheet = wb['Спецификация изделий']

        for i in range(1, sheet.max_row):
            name_var = sheet[f"C{i}"]
            product_number = sheet[f"E{i}"]
            if (name_var.value != None):
                self.name_var_1[self.file2_length] = name_var.value
                self.io[self.file2_length] = product_number.value
                self.file2_length = self.file2_length + 1

    def print(self):
        print(self.io)
        print(self.name_var)
        print(f"length: {self.file1_length}")

    def getVar(self, i):
        return self.name_var[i]

    def getIO(self, i):
        return self.io[i]