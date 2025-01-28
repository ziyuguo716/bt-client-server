import socket

client= socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("90:65:84:6B:A9:53", 4))

try:
    while True:
        message = input("Enter message from Client side: ")
        client.send(message.encode("utf-8"))
        data = client.recv(1024)
        if not data:
            break
        print(f"Message received on CLIENT SIDE: {data.decode("utf-8")}")
except OSError as e:
    pass

client.close()