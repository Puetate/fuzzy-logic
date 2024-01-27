import time
import serial

ARD_UNO=serial.Serial('COM3',9600)
while True:
    valor_analog=ARD_UNO.readline()
    v=valor_analog.decode('utf-8') #codificacion de formatos
    print("Temperatura: ",v)



    time.sleep(0.5)
ARD_UNO.close()