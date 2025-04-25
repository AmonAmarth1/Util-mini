import serial
import minimalmodbus

from time import sleep

from Literals import Literal

class DriverModbusReadDataPLC:

    def __init__(self, address=1, port='COM8', baudrate=115200, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=0.1):
        try:
            self.client1 = minimalmodbus.Instrument(port, address, debug=False)  # port name, slave address (in decimal)
            self.client1.serial.baudrate = baudrate  # baudrate
            self.client1.serial.bytesize = bytesize
            self.client1.serial.parity   = parity
            self.client1.serial.stopbits = stopbits
            self.client1.serial.timeout  = timeout      # seconds
            self.client1.address         = address        # this is the slave address number
            self.client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
            self.client1.clear_buffers_before_each_transaction = True
        except Exception as e:
            print(f"Произошло исключение: {e}")
            raise

    def closePort(self):
        self.client1.serial.close()

    def readSingleRegistr(self, reg):
        if (reg != 0 and reg != None):
            return self.client1.read_register(reg)
    def readSingleBit(self, reg):
        if (reg != 0 and reg != None):
            return self.client1.read_bit(reg)
    def readSingleLong(self, reg):
        if (reg != 0 and reg != None):
            return self.client1.read_long(reg)

    def readData(self, reg, type_reg):
        if (type_reg == 5):
            return self.readSingleBit(reg)
        if (type_reg == 6):
            return self.readSingleRegistr(reg)
        if (type_reg == 7):
            return self.readSingleLong(reg)

    def readCortageIO(self, cortage):
        value_cortage = []
        for i in range(0, len(cortage)):
            value_cortage.append(self.readSingleRegistr(cortage[i]))
        return value_cortage

