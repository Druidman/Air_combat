import socket as s
from threading import Thread
from models import Client
import json,time


class Server():
    def __init__(self):
        self.server = s.socket(s.AF_INET,s.SOCK_STREAM)
        self.server.bind(("0.0.0.0",8080))
        self.server.listen(5)

        self.client_threads = []
    

    def accept_connection(self):
        return self.server.accept()
     
    def make_client_thread(self,client):
        thread = Thread(target=self.handle_client,args=(client,))
        thread.daemon = True
        thread.start()

        return thread
    
    def listen(self):
        print("listening")
        socket, address = self.accept_connection()
        client = [socket,address]

        thread = self.make_client_thread(client)
        self.client_threads.append(thread)

    def handle_client(self,client):
        conn = client[0]
        address, port = client[1]

        client = Client(conn,address,port)
       
       

    def main(self):
        self.listen()

    




