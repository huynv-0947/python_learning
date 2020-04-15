import socket, threading
class ClientThread(threading.Thread):
  def __init__(self, client_socket, client_addr):
    threading.Thread.__init__(self) # init new thread for client connection
    self.socket = client_socket
    self.addr = client_addr
    print("New client connected: ", self.addr)

  def run(self):
    print("Connection from: ", self.addr)
    self.socket.send(bytes('Welcome to chat app!', 'UTF-8'))
    while True:
      msg = self.socket.recv(2048).decode()
      print(f"Client[{self.addr[1]}]: {msg}")

      self.to_all(msg)

  def to_all(self, msg):
    for s in sockets:
      if s != self.socket:
        s.send(bytes(msg, "UTF-8"))

# server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 8080))
sockets = []
print("Server started! Waiting for connection ...")

while True:
  server.listen(1)
  client_socket, client_addr = server.accept()
  sockets.append(client_socket)
  new_thread = ClientThread(client_socket, client_addr)
  new_thread.start()
