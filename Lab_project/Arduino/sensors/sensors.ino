void setup() {
	Serial.begin(9600);
	// put your setup code here, to run once:
	pinMode(A0,INPUT);
	pinMode(A1,INPUT);
	pinMode(A2,INPUT);
	pinMode(A3,INPUT);
	pinMode(A4,INPUT);
	pinMode(A5,INPUT);
	pinMode(A6,INPUT);
	pinMode(A7,INPUT);

	pinMode(4,OUTPUT);
	pinMode(5,OUTPUT);
	pinMode(6,OUTPUT);
	pinMode(7,OUTPUT);
	pinMode(8,OUTPUT);
	pinMode(9,OUTPUT);
	pinMode(10,OUTPUT);
	pinMode(11,OUTPUT);

	digitalWrite(4,LOW);
	digitalWrite(5,LOW);
	digitalWrite(6,LOW);
	digitalWrite(7,LOW);
	digitalWrite(8,LOW);
	digitalWrite(9,LOW);
	digitalWrite(10,LOW);
	digitalWrite(11,LOW);
}

void loop() {
	// put your main code here, to run repeatedly:

	int index=0;
	char lIncomingChar;
	char lInBuffer[4];
	for(int i = 0 ; i < sizeof(lInBuffer)/sizeof(char) ; i++)
		lInBuffer[i] = ' ';
	
	while(Serial.available() == 0)
	{
		delay(300);
	}
	while(Serial.available() > 0)
	{
		lIncomingChar = (char)Serial.read();
		if(index < 4)
			lInBuffer[index] = lIncomingChar;
		index++;
		delay(300);
	}
	if(lInBuffer[0] == 'r' && lInBuffer[1] == 'e' && lInBuffer[2] == 'a' && lInBuffer[3] == 'd')
	{
		int x[8];
		digitalWrite(4,HIGH);
		delay(10);
		x[0] = analogRead(A7);
		digitalWrite(4,LOW);
		delay(100);

		digitalWrite(5,HIGH);
		delay(10);
		x[1] = analogRead(A6);
		digitalWrite(5,LOW);
		delay(100);

		digitalWrite(6,HIGH);
		delay(10);
		x[2] = analogRead(A5);
		digitalWrite(6,LOW);
		delay(100);

		digitalWrite(7,HIGH);
		delay(10);
		x[3] = analogRead(A4);
		digitalWrite(7,LOW);
		delay(100);

		digitalWrite(8,HIGH);
		delay(10);
		x[4] = analogRead(A3);
		digitalWrite(8,LOW);
		delay(100);

		digitalWrite(9,HIGH);
		delay(10);
		x[5] = analogRead(A2);
		digitalWrite(9,LOW);
		delay(100);

		digitalWrite(10,HIGH);
		delay(10);
		x[6] = analogRead(A1);
		digitalWrite(10,LOW);
		delay(100);

		digitalWrite(11,HIGH);
		delay(10);
		x[7] = analogRead(A0);
		digitalWrite(11,LOW);
		delay(100);

		Serial.print(x[0]);
		Serial.print('\t');
		Serial.print(x[1]);
		Serial.print('\t');
		Serial.print(x[2]);
		Serial.print('\t');
		Serial.print(x[3]);
		Serial.print('\t');

		Serial.print(x[4]);
		Serial.print('\t');
		Serial.print(x[5]);
		Serial.print('\t');
		Serial.print(x[6]);
		Serial.print('\t');
		Serial.println(x[7]);
		Serial.println("");

	}
	else
	{
		Serial.println(lInBuffer);
	}
}

