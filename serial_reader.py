import serial


PORT = "/dev/ttyUSB0"
BAUDRATE = 115200

def read() -> float:
    value = None

    with serial.Serial(PORT, BAUDRATE, timeout=1) as reader:
        line = reader.readline()
        value = float(line.split("\r\n")[0])

        return value
