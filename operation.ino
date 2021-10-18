// 设定SR04连接的Arduino引脚
const int TrigPin1 = 10;
const int EchoPin1 =11;
const int TrigPin2 = 9;
const int EchoPin2 =8;

//motor 
int IN1 = 6;   
int IN2 = 7;  


char rec;

//float distance1;
//float distance2;

void setup() {
  // 初始化串口通信及连接SR04的引脚
  // 要检测引脚上输入的脉冲宽度，需要先设置为输入状态
  Serial.begin(9600);
  
  pinMode(TrigPin1, OUTPUT);
  pinMode(TrigPin2, OUTPUT);
  pinMode(EchoPin1, INPUT);
  pinMode(EchoPin2, INPUT);
  Serial.println("Ultrasonic sensor");

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  Serial.println("MOTOR");
}

void Drive(){
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  }

void Reverse(){
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  }
void Park(){
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,HIGH);
  }

float avoid1(){
  // 产生一个10us的高脉冲去触发TrigPin
      digitalWrite(TrigPin1, LOW);
      delayMicroseconds(2);
      digitalWrite(TrigPin1, HIGH);
      delayMicroseconds(10);
      digitalWrite(TrigPin1, LOW);
  // 检测脉冲宽度，并计算出距离
      float distance1;
      distance1 = pulseIn(EchoPin1, HIGH) / 58.00;
      Serial.print(distance1);
      Serial.print("cm");
      Serial.println();
      return distance1;
  }
float avoid2(){
    // 产生一个10us的高脉冲去触发TrigPin
    digitalWrite(TrigPin2, LOW);
    delayMicroseconds(2);
    digitalWrite(TrigPin2, HIGH);
    delayMicroseconds(10);
    digitalWrite(TrigPin2, LOW);
    // 检测脉冲宽度，并计算出距离
    float distance2;
    
    distance2 = pulseIn(EchoPin2, HIGH) / 58.00;
    Serial.print(distance2);
    Serial.print("cm");
    Serial.println();
    return distance2;
  }

unsigned long time=1000;
void loop() {

  float dis1;
  float dis2;
  
  if(Serial.available()){
    rec=Serial.read();
    Serial.println(rec);
  }

  if(rec=='D'){
    dis1=avoid1();
    while(dis1>=30){
      Drive();
      dis1=avoid1();
      }
   Park();
    }
  if(rec=='R'){
    dis2=avoid2();
    while(dis2>=30){
      Reverse();
      dis2=avoid2();
      }
    Park();
    }
  delay(time);
}
