#define TRIG_PIN 9
#define ECHO_PIN 10
#define DIST_THRESHOLD 15 // distance in cm
#define LED_PIN 13       // LED on pin 13 as trigger example

unsigned long previousMillis = 0;  // To store the time of the previous trigger
unsigned long currentMillis = 0;   // To store the time of the current trigger
float strokesPerMinute = 0;        // To store the calculated strokes per minute
bool mDetected = false;   // State variable to track coin detection
void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  long duration, distance;
  
  // Send out a pulse from the ultrasonic sensor
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  // Measure the pulse duration from the Echo pin
  duration = pulseIn(ECHO_PIN, HIGH);
  
  // Calculate the distance in centimeters
  distance = (duration * 0.034) / 2;

  // Display the distance in the Serial Monitor
  //Serial.print("Distance: ");
  //Serial.println(distance);

  // If the distance is less than or equal to the threshold, trigger action
  if (distance <= DIST_THRESHOLD) {
    digitalWrite(LED_PIN, HIGH);  // Trigger action (e.g., LED on)
    
    // Calculate the strokes per minute when the LED turns on
    currentMillis = millis();  // Get the current time in milliseconds
    if (previousMillis > 0 && !mDetected) {  // Ensure this is not the first trigger
      unsigned long timeDifference = currentMillis - previousMillis;  // Time between triggers in milliseconds
      float timeDifferenceMinutes = timeDifference / 60000.0;  // Convert to minutes
      strokesPerMinute = 1 / timeDifferenceMinutes;  // Calculate strokes per minute
      //Serial.print("Strokes per minute: ");
      if (strokesPerMinute > 10 && strokesPerMinute < 120)
      Serial.println(strokesPerMinute);
      //Serial.print("t: ");
      //Serial.println(timeDifference);
      //Serial.print("tm: ");
      //Serial.println(timeDifferenceMinutes);

      
      mDetected = true;
    }
    previousMillis = currentMillis;  // Update the time of the last trigger
  }  else {
    digitalWrite(LED_PIN, LOW);   // Turn off LED
    mDetected = false;  // Reset detection flag
  }

  delay(300);  // Small delay to avoid spamming the sensor
}
