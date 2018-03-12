const int trigPin =9;
const int echoPin =10;
long duration;
int distance;

void setup() {
  // put your setup code here, to run once:
pinMode(trigPin,OUTPUT);
pinMode(echoPin,INPUT);
Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);

  duration =pulseIn(echoPin,HIGH);
  distance =duration*0.034/2;

   int sensorValue=analogRead(A0);
  // Serial.print("The CO detector value is");
   
   Serial.print(sensorValue);
   Serial.print(",");
  if(distance>400 ||distance<2)
  {
    Serial.println("out of range");
  }
  else
  {
  Serial.println(distance);
 delay(500);
  }
  delay(500);
  // put your main code here, to run repeatedly:
}
