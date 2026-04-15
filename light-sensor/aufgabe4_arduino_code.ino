void setup() {
  // Ich initialisiere die serielle Kommunikation mit 9600 Baud
  Serial.begin(9600);
}

void loop() {
  // Ich lese den analogen Wert vom Lichtsensor am Eingang A0
  int value = analogRead(A0);

  // Ich sende den Messwert über die serielle Schnittstelle an den PC
  Serial.println(value);

  // Ich warte eine Sekunde bis zur nächsten Messung
  delay(1000);
}
