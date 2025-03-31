
from Literals import Literal

LENGTH_DATA_OUTPUT = 4
POSITION_BIN_DIGITAL_OUTPUT = 3
class DataPLC:

    def __init__(self):
        self.data_io_for_modbus = []
        self.data_io_var = []
        self.data_io = []
        self.length = 0
        self.bin_digital = 0


    def addDataIOModbus(self, item):
        self.data_io_for_modbus.append(item)
        self.length = self.length + 1

    def addDataVarIO(self, item):
        self.data_io_var.append(item)

    def addDataIO(self, item):
        self.data_io.append(item)

    def clear(self):
        self.data_io_for_modbus.clear()
        self.data_io_var.clear()
        self.data_io.clear()
        self.length = 0
        self.bin_digital = Literal.DEFAULT_BIN_OUTPUT_DIGIT

    def print(self):
        print(self.data_io_for_modbus)
        print(self.data_io_var)
        print(self.data_io)
        print(self.length)
        print(self.bin_digital)

    def setBinDigital(self):
        for i in range(1, self.length):
            if(self.data_io_for_modbus[i] != None):
                if (len(self.data_io_for_modbus[i]) == LENGTH_DATA_OUTPUT):
                    self.bin_digital = self.bin_digital | self.data_io_for_modbus[i][POSITION_BIN_DIGITAL_OUTPUT][0]


    def getBinDigital(self):
        return self.bin_digital

    def getData(self):
        return self.data_io_for_modbus

    def getLength(self):
        return self.length