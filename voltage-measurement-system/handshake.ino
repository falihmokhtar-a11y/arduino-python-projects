int sensorPin = A0;    // select the input pin 
int outPin = 7;      // select the pin for the output
int ledPin = 13; // visual command indicator
void setup() {
  // initialize serial communication at 115200 bits per second to match that of the python script:
  Serial.begin(115200);
  pinMode(outPin,OUTPUT);
  digitalWrite(outPin,LOW);
   
#if 0
  pinMode(inputPin,INPUT_PULLUP)
  pinMode(inputPin,INPUT)
  val = digitalRead(inputPin)
#endif
}

void loop() {
  // read the input on analog pin 0 when "s" is sent from Python  
  if(Serial.available()){
    char data = Serial.read();
    if (data == 's'){
      digitalWrite(ledPin,!digitalRead(ledPin));
      Serial.println(analogRead(sensorPin));
      Serial.flush();
      delay(1);        // delay in between reads for stability
    }else if (data == 'h'){
      digitalWrite(outPin,HIGH);
      digitalWrite(ledPin,HIGH);
      Serial.println("on");
      Serial.flush();
      delay(1);        // delay in between reads for stability
    } else if (data == 'l'){
      Serial.println("off");
      Serial.flush();
      digitalWrite(ledPin,HIGH);
      digitalWrite(outPin,LOW);
      delay(100);
      digitalWrite(ledPin,HIGH);
      delay(130);
      digitalWrite(ledPin,LOW);
      delay(100);
      digitalWrite(ledPin,HIGH);
      delay(130);
      digitalWrite(ledPin,LOW);
      delay(100);
      digitalWrite(ledPin,HIGH);
      delay(130);
      digitalWrite(ledPin,LOW);
      delay(100);
      digitalWrite(ledPin,HIGH);
      delay(130);
      digitalWrite(ledPin,LOW);      
    }
  }
}
