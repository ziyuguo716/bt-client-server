import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
#server.bind(("90:65:84:6B:A9:53", 4))
server.bind(("F8:9E:94:6B:91:02", 4))
server.listen(3)

conn, addr = server.accept()
print(f"Connection from {addr}")

filename = 'received.txt'
with open(filename, 'wb') as file:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        file.write(data)

print(f"File received and saved as {filename}")
conn.close()
server.close()