import time
from machine import I2C, Pin
from ds3231 import DS3231

i2c = I2C(0, scl=Pin(9), sda=Pin(8))
rtc = DS3231(machine.I2C(0))

while True:
    tt = rtc.get_time()
    print("Año: {:04d} Mes: {:02d} Dia: {:02d} | H-M-S: {:02d}:{:02d}:{:02d}".format(*tt))
    time.sleep(1)
