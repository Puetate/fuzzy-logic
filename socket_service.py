import socketio

class SocketService:
    def __init__(self, server_addres,port) :
        self.server_addres = server_addres
        self.port = port
        self.sio = socketio.Client()
        
        @self.sio.event
        def connect():
            print('Conexión exitosa al servidor Node.js')

        @self.sio.event
        def disconnect():
            print('Desconectado del servidor Node.js')
            
        self.connect()

    def connect(self):
        self.sio.connect(f'{self.server_addres}:{self.port}')

    def emit_message(self, key, mensaje):
        self.sio.emit(key, mensaje)

    def disconnect_socket(self):
        self.sio.disconnect()