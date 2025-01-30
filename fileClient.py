import socket

client= socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("F8:9E:94:6B:91:02", 4))
print("Connected.")

filename = 'example.txt'
with open(filename, 'rb') as file:
    while (chunk := file.read(1024)):
        client.sendall(chunk)

print("File sent successfully")
client.close()