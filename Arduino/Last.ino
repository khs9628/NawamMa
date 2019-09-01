#include <ArduinoJson.h>

// LED를 핀에 연결합니다. 5개 각 좌석과 연동
int LED = 3;
int LED2 = 5;
int LED3 = 6;
int LED4 = 9;
int LED5 = 10; 
int speakerPin = 11;
int LEDP = 4; 
int length = 15;



char notes[] = "ccggaag ffeeddc ggffeed ggffeed ccggaag ffeeddc "; 
int beats[] = { 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 4 };
int tempo = 300;

void playTone(int tone, int duration) {
  for (long i = 0; i < duration * 1000L; i += tone * 2) {
    digitalWrite(speakerPin, HIGH);
    delayMicroseconds(tone);
    digitalWrite(speakerPin, LOW);
    delayMicroseconds(tone);
  }
}

void playNote(char note, int duration) {
  char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
  int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014, 956 };
  
  for (int i = 0; i < 8; i++) {
    if (names[i] == note) {
      playTone(tones[i], duration);
    }
  }
}

void setup() {
  // 센서값을 측정하기위해 시리얼통신을 준비합니다.
  Serial.begin(9600); 
  pinMode(speakerPin, 64);
  
}

void loop() {
   while(Serial.available()) {
   char ch = Serial.read(); 
    if( ch == 'p') {
      digitalWrite(LEDP, HIGH); 
      for (int i = 0; i < length; i++) {
          if (notes[i] == ' ') {
            delay(beats[i] * tempo);
          } else {
            playNote(notes[i], beats[i] * tempo);
          }
            delay(tempo / 2); 
         }
     digitalWrite(LEDP, LOW);
     Serial.println("T");
    } 
   }
  //아날로그 핀에 압력센서를 연결합니다. 5개  
  int seat = analogRead(A0);
  int seat2 = analogRead(A1);
  int seat3 = analogRead(A2);
  int seat4 = analogRead(A3);
  int seat5 = analogRead(A4);
 
  // 0부터 1023의 센서값을 PWM 값 범위(0-255)로 변환 합니다.
  int brightness = map(seat, 0 , 1023, 0, 255);
  int brightness2 = map(seat2, 0 , 1023, 0, 255);
  int brightness3 = map(seat3, 0 , 1023, 0, 255);
  int brightness4 = map(seat4, 0 , 1023, 0, 255);
  int brightness5 = map(seat5, 0 , 1023, 0, 255);
  
  // 아날로그 입력을 통해 LED를 밝기를 조절합니다..
  analogWrite(LED,brightness);
  analogWrite(LED2,brightness2);
  analogWrite(LED3,brightness3);
  analogWrite(LED4,brightness4);
  analogWrite(LED5,brightness5); 
  
  //시리얼 모니터를 통해 센서값을 표기합니다. 
  Serial.print("{\"seat\": \""); Serial.print(seat); Serial.print("\", ");
  Serial.print("\"seat2\": \""); Serial.print(seat2); Serial.print("\", ");
  Serial.print("\"seat3\": \""); Serial.print(seat3); Serial.print("\", ");
  Serial.print("\"seat4\": \""); Serial.print(seat4); Serial.print("\", ");
  Serial.print("\"seat5\": \""); Serial.print(seat5); Serial.println("\"}");

//  
  delay(5000);
}
