const BluetoothSerialPort = require('bluetooth-serial-port').BluetoothSerialPort;

const btSerial = new BluetoothSerialPort();
const address = "F8:9E:94:6B:91:02"; // Replace with the correct address of the server
const port = 4;  // RFCOMM port number

btSerial.connect(address, port, () => {
    console.log("Connected to server!");

    process.stdin.resume();
    process.stdin.setEncoding('utf8');

    process.stdin.on('data', function (message) {
        btSerial.write(new Buffer(message, 'utf-8'), (err, bytesWritten) => {
            if (err) {
                console.log("Error sending message:", err);
            } else {
                console.log("Message sent, waiting for response...");
            }
        });

        btSerial.on('data', function (buffer) {
            console.log("Message received on CLIENT SIDE: " + buffer.toString('utf-8'));
        });
    });
});

btSerial.on('error', function (err) {
    console.log("Error:", err);
});

