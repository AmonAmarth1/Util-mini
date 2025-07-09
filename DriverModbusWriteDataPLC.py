import serial
import minimalmodbus

from time import sleep

from Literals import Literal
class DriverModbusWriteDataPLC:

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

    def writeSingleData(self, value, num_reg, type_reg = 6):
        try:
            if (num_reg != None and value != None and num_reg != 0):
                if(type_reg == 5):
                    print(f"nume reg: {num_reg}, value: {value}, type reg: 5;")
                    self.client1.write_bit(num_reg, value)
                if (type_reg == 6):
                    print(f"nume reg: {num_reg}, value: {value}, type reg: 6;")
                    self.client1.write_register(num_reg, value, number_of_decimals=0, functioncode=6)
                if (type_reg == 7):
                    print(f"nume reg: {num_reg}, value: {value}, type reg: 7;")
                    self.writeLong(num_reg, value)
        except Exception as e:
            print(f"Произошло исключение: {e}")
            raise

    def sendCortage(self, data):
        if (data != None):
            for i in range(0, len(data)):
                if(len(data[i]) == 3):
                    self.writeSingleData(data[i][0], data[i][1], data[i][2])
                if (len(data[i]) == 2 and data[i][1] != Literal.reg_bin_digit):
                    self.writeSingleData(data[i][0], data[i][1])


    def sendArray(self, data):
        try:
            for i in range(0, len(data)):
                print(f"i: {i}")
                self.sendCortage(data[i])
        except Exception as e:
            print(f"Произошло исключение: {e}")
            raise
        return 0

    def writeLong(self, reg, value):
        try:
            if (reg != None and value != None and reg != 0):
                print(f"reg: {reg}, value: {value}")
                self.client1.write_long(reg, value)
        except Exception as e:
            print(f"Произошло исключение: {e}")
            raise



