#include <LiquidCrystal.h>

// LCD pin configuration
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// Sensor pins
const int ecPin = A0;
const int phPin = A1;
const int tempPin = A2; // Use analog pin A2 for TMP36

// LEDs
const int greenLed = 7;
const int redLed = 8;

// Define plant types
enum PlantType { LETTUCE, TOMATOES, SPINACH, BASIL, PEPPERS, CUCUMBERS };
PlantType currentPlant = TOMATOES; // Default to TOMATOES if invalid selection

// Plant names for display
const char* plantNames[] = {"Lettuce", "Tomatoes", "Spinach", "Basil", "Peppers", "Cucumbers"};

// Balancing recommendations
struct BalanceRecommendation {
  float idealEC;
  float idealPH;
  float idealTemp;
  const char* suggestion;
};

BalanceRecommendation balanceRecommendations[] = {
  {1.2, 6.0, 20, "Add more nutrients"},
  {2.0, 6.5, 25, "Adjust pH slightly"},
  {1.8, 6.2, 22, "Increase temperature"},
  {1.5, 6.0, 23, "Reduce nutrients slightly"}, // BASIL
  {1.8, 6.0, 24, "Check pH and EC levels"},   // PEPPERS
  {2.2, 6.5, 26, "Increase nutrients and temperature"} // CUCUMBERS
};

void setup() {
  // Initialize LCD
  lcd.begin(16, 2);

  // Initialize LEDs
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);

  // Start Serial communication for debugging
  Serial.begin(9600);

  // Display plant selection for user
  Serial.println("Select Plant:");
  Serial.println("0: Lettuce");
  Serial.println("1: Tomatoes");
  Serial.println("2: Spinach");
  Serial.println("3: Basil");
  Serial.println("4: Peppers");
  Serial.println("5: Cucumbers");
  Serial.print("Enter plant index (0-5): ");
}

void loop() {
  if (Serial.available() > 0) {
    int plantIndex = Serial.parseInt();
    if (plantIndex >= 0 && plantIndex <= 5) {
      currentPlant = static_cast<PlantType>(plantIndex);
      Serial.print("Selected Plant: ");
      Serial.println(plantNames[plantIndex]);
    } else {
      Serial.println("Invalid selection, defaulting to Tomatoes.");
      currentPlant = TOMATOES;
    }

    // Check the nutrient balance for the selected plant
    checkNutrientBalance();

    // Wait for user input to proceed to the next plant selection
    Serial.println("Press any key to check another plant.");
    while (Serial.available() == 0) {}
    Serial.read(); // Clear the input buffer

    // Display plant selection for user again
    Serial.println("Select Plant:");
    Serial.println("0: Lettuce");
    Serial.println("1: Tomatoes");
    Serial.println("2: Spinach");
    Serial.println("3: Basil");
    Serial.println("4: Peppers");
    Serial.println("5: Cucumbers");
    Serial.print("Enter plant index (0-5): ");
  }
}

void checkNutrientBalance() {
  // Read EC value
  int ecValue = analogRead(ecPin);
  float ecVoltage = ecValue * (5.0 / 1023.0);
  float ec = (ecVoltage - 0.5) * 10.0; // Simplified conversion

  // Read pH value
  int phValue = analogRead(phPin);
  float phVoltage = phValue * (5.0 / 1023.0);
  float ph = 3.5 * phVoltage; // Simplified conversion

  // Read Temperature
  int tempValue = analogRead(tempPin);
  float voltage = tempValue * (5.0 / 1023.0);
  float temperature = (voltage - 0.5) * 100; // TMP36: 10 mV per degree Celsius, 500 mV offset

  // Debugging print statements
  Serial.print("Raw EC Value: ");
  Serial.println(ecValue);
  Serial.print("Raw pH Value: ");
  Serial.println(phValue);
  Serial.print("Raw Temperature Value: ");
  Serial.println(tempValue);

  Serial.print("EC Voltage: ");
  Serial.println(ecVoltage, 2);
  Serial.print("pH Voltage: ");
  Serial.println(phVoltage, 2);
  Serial.print("Temperature Voltage: ");
  Serial.println(voltage, 2);

  Serial.print("EC: ");
  Serial.println(ec, 2);
  Serial.print("pH: ");
  Serial.println(ph, 2);
  Serial.print("Temperature: ");
  Serial.println(temperature, 1);

  // Determine nutrient balance based on plant type
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(plantNames[currentPlant]);
  lcd.setCursor(0, 1);

  switch (currentPlant) {
    case LETTUCE:
    case TOMATOES:
    case SPINACH:
      
      digitalWrite(greenLed, HIGH);
      digitalWrite(redLed, LOW);
      lcd.print("Balanced");
      Serial.println("Nutrient balance: Balanced");
      break;
    case BASIL:
    case PEPPERS:
    case CUCUMBERS:
      
      digitalWrite(greenLed, LOW);
      digitalWrite(redLed, HIGH);
      lcd.print("Imbalance");
      Serial.println("Nutrient balance: Imbalanced");

      // Display recommendation
      BalanceRecommendation rec = balanceRecommendations[currentPlant];
      Serial.print("Recommendation: ");
      Serial.println(rec.suggestion);
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Adjust to:");
      lcd.setCursor(0, 1);
      lcd.print("EC ");
      lcd.print(rec.idealEC);
      lcd.print(" pH ");
      lcd.print(rec.idealPH);
      delay(2000); // Display for 2 seconds

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Temp: ");
      lcd.print(rec.idealTemp);
      lcd.print(" C");
      lcd.setCursor(0, 1);
      lcd.print(rec.suggestion);
      delay(5000); // Display for 5 seconds
      break;
  }

  delay(5000); // Delay for 5 seconds before rechecking
}
