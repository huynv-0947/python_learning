import socket
import sys
import select

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))

while True:
  readable, _, _ = select.select([sys.stdin, client], {}, {})
  for read in readable:
    if read == client: # received from server
      print(client.recv(2048).decode())
    else:
      msg = input("> ")
      client.send(bytes(msg, 'UTF-8'))

client.close()
