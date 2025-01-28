import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("90:65:84:6B:A9:53", 4))
server.listen(1)

client, addr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message Received on SERVER side: {data.decode('utf-8')}")
        message = input ("ENTER MESSAGE ON SERVER SIDE:")
        client.send(message.encode("utf-8"))
except OSError as e:
    pass

client.close()
server.close()