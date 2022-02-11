import socket

HOST = ''
PORT = 6969

def start():
  global server_socket
  server_socket = socket.socket()
  server_socket.bind((HOST, PORT))
  server_socket.listen(1) #max 1 unaccepted connection
  

def connect():
  conn, addr = server_socket.accept() #waits for a connection
  while True:
    with conn.recv(1024) as data:
      if not data:
        break
      print(data.decode("utf-8"))

start()
connect()
