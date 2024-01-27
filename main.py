import serial
from fuzzy_logic_aquarium import FuzzyLogicAquarium
from socket_service import SocketService

ADDRES_SERVER = 'http://127.0.0.1'
SERVER_PORT = 3000


def main():
    fuzzy_logic = FuzzyLogicAquarium()
    socket = SocketService(ADDRES_SERVER, SERVER_PORT)

    ARD_UNO=serial.Serial('COM3',9600)
    while True:
        valor_analog=ARD_UNO.readline()
        temperatura=valor_analog.decode('utf-8')
        temperatura = round(float(temperatura))
        fuzzy_logic.new_temperature(temperatura)
        potencia_calentador = fuzzy_logic.potencia_calentador
        potencia_ventilador = fuzzy_logic.potencia_ventilador
        outputs = {'temperature': temperatura,
                   'fab': potencia_ventilador, 
                   'heater': potencia_calentador}
        socket.emit_message('input-fuzzed', outputs)
        print("Temperatura:", temperatura)
        print("El potencia ventilador es:", potencia_calentador)
        print("La potencia del calentador es:", potencia_ventilador)


if __name__ == "__main__":
    main()
