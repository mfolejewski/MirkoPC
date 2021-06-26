# coding: utf-8

import smbus

#tpa6130a2 i2c address 
i2c_addr = 0x60

print("TPA6130A2 init")


#read tpa6130a2 version
def tpa6130a2_version(): 
    bus = smbus.SMBus(1)
    data = bus.read_word_data(i2c_addr, 4)
    data = data & 0x0f
    return data

#init tpa6130a2
def tpa6130a2_init(): 
    bus = smbus.SMBus(1)
    bus.write_word_data(i2c_addr, 1, 0xc0)
    bus.write_word_data(i2c_addr, 2, 0x35)
    bus.write_word_data(i2c_addr, 3, 0x00)
    return 0

if (tpa6130a2_version() == 0x02):
    print("TPA6130A2 present on the I2C interface")
    tpa6130a2_init();
else:
    print("TPA6130A2 not found on the I2C interface")
