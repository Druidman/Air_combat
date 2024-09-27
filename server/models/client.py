import socket

class Client():
    def __init__(self,conn: socket.socket,address: str,port:int):
        self.conn = conn
        self.address = address
        self.port = port

    def send_data(self): pass

    def receive_data(self): pass

    def main(self): pass
