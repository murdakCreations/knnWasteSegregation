#include <SoftwareSerial.h>
#include <Wire.h>
SoftwareSerial sim(10, 11);

void setup() {
  Serial.begin(9600);
  sim.begin(9600);
  delay(1000);
}

void loop() {
  testGSM();
  delay(200);
  //Serial.println("\n200 msec");
  /*testGSM2();
  displayStat();
  delay(10000);
  Serial.println("10 sec");
  
  /*sendSMS();
  delay(10000);
  displayStat();*/
}

void displayStat(){
  if (sim.available() > 0){
  Serial.write(sim.read());}
}

void testGSM(){
  sim.write("\nAT+CMGF=1\n");
  delay(200);
  displayStat();
  
}

void testGSM2(){
  sim.println("\nAT+CMGF=0\n");
  delay(60000);
}

void sendSMS(){
  sim.write("\nAT+CMGS=\"+639355667198\"\r\n");
  delay(6000);
  sim.write("hello there\n The bin is full");
  delay(6000);
  sim.write((char)26);
  delay(6000); 
}