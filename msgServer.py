import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.connect(("F8:9E:94:6B:91:02", 4))
server.listen(3)

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