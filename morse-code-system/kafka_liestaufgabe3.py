import serial # type: ignore
import time
from morsen import encode

PORT = "COM8"   # Ich definiere den verwendeten COM-Port   

BAUD = 115200  # Ich lege die Baudrate für die serielle Kommunikation fest

# Ich öffne die Textdatei und lese den gesamten Inhalt ein
with open("kafka.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Ich kodiere den gelesenen Text in Morsecode
morse_code = encode(text)

# Ich stelle eine serielle Verbindung zum Arduino her
with serial.Serial(PORT, BAUD, timeout=1) as ser:
    time.sleep(2)
# Ich sende den Morsecode über die serielle Schnittstelle    
    ser.write((morse_code + "\n").encode("utf-8"))