import machine
import utime

sens_temp = machine.ADC(4)
conv_fact = 3.3 / (65535)

while True:
    reading = sens_temp.read_u16() * conv_fact
    temp = 27 - (reading - 0.706) / 0.001721
    print(temp)
    utime.sleep(2)
    