//Sliders init
const int NUM_SLIDERS = 5;
const int analogInputs[NUM_SLIDERS] = {A0, A1, A2, A3, A4};
int analogSliderValues[NUM_SLIDERS];
//End slider init

//Keypad init
byte inputs[] = {6,7,8,9};
const int inCount = sizeof(inputs)/sizeof(inputs[0]);
byte outputs[] = {2,3,4,5};
const int outCount = sizeof(outputs)/sizeof(outputs[0]);

int longPressDelay = 350;           //customizable encoderValues
int spamSpeed = 15;

int layout[4][4] = {               //layout grid for characters
  {1,2,3,4},
  {5,6,7,8},
  {9,10,11,12},
  {13,14,15,16},
};
int keyDown[4][4];
bool keyLong[4][4];
//Keypad end

void setup() {
  //slider setup
  for (int i = 0; i < NUM_SLIDERS; i++) {
    pinMode(analogInputs[i], INPUT);
  }
  //end
  //keypad setup
  pinMode(2, INPUT);
  pinMode(0, INPUT);

  for(int i=0; i<outCount; i++){    //declaring all the outputs and setting them high
    pinMode(outputs[i],OUTPUT);
    digitalWrite(outputs[i],HIGH);
  }
  for(int i=0; i<inCount; i++){     //declaring all the inputs and activating the internal pullup resistor
    pinMode(inputs[i],INPUT_PULLUP);
  }
  //end
  Serial.begin(9600);
}

void loop() {
  updateSliderValues();
  String sliderValues = buildSliderValueString();

  for (int i=0; i<4; i++)
  {
    digitalWrite(outputs[i],LOW);   //setting one row low
    delayMicroseconds(5);           //giving electronics time to settle down

    for(int j=0; j<4; j++)
    {
      if(digitalRead(inputs[j]) == LOW)
      {           //calling keyPressed function if one of the inputs reads low
        keyPressed(i,j);
      }
      else if(keyDown[i][j] != 0)   //resetting the key if it is not pressed any more
      {
        resetKey(i,j);
      }
    }

    digitalWrite(outputs[i],HIGH);
    delayMicroseconds(500);//setting the row high and waiting 0.5ms until next cycle
  }

  Serial.println("SLIDERINFO-" + sliderValues);

  delay(100);
}

void updateSliderValues() {
  for (int i = 0; i < NUM_SLIDERS; i++) {
     analogSliderValues[i] = analogRead(analogInputs[i]);
  }
}

String buildSliderValueString() {
  String builtString = String("");

  for (int i = 0; i < NUM_SLIDERS; i++) {
    builtString += String((int)analogSliderValues[i]);

    if (i < NUM_SLIDERS - 1) {
      builtString += String("|");
    }
  }

  return builtString;
}

void printSliderValues() {
  for (int i = 0; i < NUM_SLIDERS; i++) {
    String printedString = String("Slider #") + String(i + 1) + String(": ") + String(analogSliderValues[i]) + String(" mV");
    Serial.write(printedString.c_str());

    if (i < NUM_SLIDERS - 1) {
      Serial.write(" | ");
    } else {
      Serial.write("\n");
    }
  }
}

//if a key is pressed, this Funtion is called and outputs to serial the key location, it also sends the keystroke if not already done so
void keyPressed(int row, int col){
  Serial.print("KEYPRESS-");
  Serial.println(layout[row][col]);
  if(keyDown[row][col]==0){         //if the function is called for the first time for this key

  }
  else if(keyLong[row][col] && keyDown[row][col] > spamSpeed){ //if the key has been held long enough to warrant another keystroke set
    keyDown[row][col] = 1;
  }
  else if(keyDown[row][col] > longPressDelay){ //if the key has been held for longer that longPressDelay, it switches into spam mode
    keyLong[row][col] = true;
  }

  keyDown[row][col]++;
}

void resetKey(int row, int col){ //resetting the variables after key is released
  keyDown[row][col] = 0;
  keyLong[row][col] = false;
}
