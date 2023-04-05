#Si los datos de fecha y tiempo estan incorrectos ejecuta primero este programa en tu raspbery Pi Pico y pon los datos correctos 

import machine
from ds3231 import DS3231

rtc = DS3231(machine.I2C(0))

# Obtener fecha y hora actual
now = rtc.get_time()

# Modificar fecha y hora
new_datetime = (now[0], now[1], now[2], 14, 30, 0, 0, 0)
rtc.set_time(new_datetime)

# Verificar que se ha modificado correctamente
print(rtc.get_time())
