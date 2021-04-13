# coding: utf-8

import smbus

#LM75 i2c address 
i2c_addr = 0x48

#read LM75 temperature
def read_lm75_temp(): 
    bus = smbus.SMBus(1)
    data = bus.read_word_data(i2c_addr, 0)
    data = (((data << 8) & 0xff00) | (data >> 8)) >> 5
    temp = 0.125 * ((-128 * (data & 0x400)) + (data & (~0x4000)))
    return temp
#print result
print("LM75B (U802) -> current temperature = %.3f °C" % (read_lm75_temp()))
