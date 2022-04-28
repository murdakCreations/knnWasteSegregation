#include <SoftwareSerial.h>
#include <Wire.h>
SoftwareSerial sim(10, 11);

//String categories = ["paper","plastic","glass","metal","cardboard"];
void setup() {
  // put your setup code here, to run once:
  Wire.begin(0x8);
  Serial.begin(9600);
  sim.begin(9600);
  delay(1000);
  Wire.onReceive(receiveCategory);
  delay(100);
  //sim.println("AT+CMEE=1");
  //delay(10000);
}

void loop() {
  
  // put your main code here, to run repeatedly:
  /*if (Serial.available() > 0)
    switch (Serial.read())
    {
      case 't':
        testGSM();
        break;
      case 's':
        testGSM2();
        break;
      case 'r':
        sendSMS();
        break;
    }
  
  if (sim.available() > 0)
  Serial.write(sim.read());*/
}

void testGSM(){
  sim.println("AT+CMGF=1");
  delay(200);
}

void testGSM2(){
  sim.println("AT+CMGF=0");
  delay(200);
}

void sendSMS(){
  sim.write("AT+CMGS=\"+639267035052\"\r\n");
  delay(100);
  sim.write("aaa");
  delay(100);
  sim.write((char)26);
  delay(100); 
}

void receiveCategory(int byteCounts){
  while(Wire.available()){// loop through all but the last
    char c = Wire.read(); // receive byte as a character
    c = c + '0';
    if (c == '0'){
      Serial.print('paper');     
    }
    else if (c == '1'){
      Serial.print('plastic');     
    }
    else if (c == '2'){
      Serial.print('glass');     
    }
    else if (c == '3'){
      Serial.print('metal');     
    }
    else if (c == '4'){
      Serial.print('cardboard');     
    }

    // add '0' to convert int to char
    Serial.print(c);
  }
}
