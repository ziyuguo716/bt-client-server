const BluetoothSerialPort = require('bluetooth-serial-port').BluetoothSerialPort;

const btSerial = new BluetoothSerialPort();
const port = 4; // RFCOMM port number

btSerial.listen(function (clientAddress) {
    console.log(`Client connected from: ${clientAddress}`);

    btSerial.on('data', function (buffer) {
        console.log("Message Received on SERVER side: " + buffer.toString('utf-8'));

        process.stdin.resume();
        process.stdin.setEncoding('utf8');

        process.stdin.on('data', function (message) {
            btSerial.write(new Buffer(message, 'utf-8'), (err, bytesWritten) => {
                if (err) {
                    console.log("Error sending message:", err);
                } else {
                    console.log("Message sent back to client");
                }
            });
        });
    });
});

btSerial.listen(function (clientAddress) {
    console.log(`Server is listening on RFCOMM port ${port}`);
});
