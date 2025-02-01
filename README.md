# Client Server Messaging via Bluetooth
## Step-by-Step Guide

1. Two(2) Windows/Linux machines are required for client server message exchange to work.
2. Before running either `msgClient.py` or `msgServer.py`, you will need to change the MAC Address at https://github.com/ziyuguo716/bt-client-server/blob/main/client.py#L4 and https://github.com/ziyuguo716/bt-client-server/blob/main/server.py#L4
3. To find the MAC address used by Bluetooth on the server computer. Simply open Terminal on the server computer and run `sudo ls -l /var/lib/bluetooth/`
4. Once MAC adress is updated. Pair both client and server computer via bluetooth.
5. Finally, run `msgServer.py` on the server computer and run `msgClient.py` on the client computer.
