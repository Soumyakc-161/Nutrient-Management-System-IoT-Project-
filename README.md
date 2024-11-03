# Nutrient Management System (IoT Project) 🌱

## Overview
The Nutrient Management System is an Internet of Things (IoT) project designed to manage nutrient levels in a hydroponic setup. Using sensors and an Arduino, this system monitors and displays essential plant-growing parameters—EC (Electrical Conductivity), pH, and temperature—to ensure optimal plant health. The system provides real-time feedback on nutrient balance, with an LED indicator signaling balanced (green) or imbalanced (red) conditions.

This project is ideal for small-scale indoor or home hydroponic systems, aiding growers in maintaining nutrient balance, which is crucial for plant growth and productivity.

## Features
- **Real-Time Monitoring:** Continuously reads EC, pH, and temperature.
- **Plant-Specific Settings:** Users can select a plant (lettuce, tomatoes, spinach, basil, peppers, or cucumbers), with nutrient requirements adjusted accordingly.
- **LED Indicator:** A green LED turns on for a balanced nutrient environment, and a red LED lights up for imbalances, along with display alerts.
- **User Alerts:** If nutrient levels deviate from optimal ranges, an alert is displayed with corrective recommendations.
- **User-Friendly Interface:** Display readings and alerts on an LED screen, making monitoring easy.

---

## Components Used
- **Arduino Uno**: Main microcontroller to process sensor data and control outputs.
- **EC Sensor**: Measures electrical conductivity to estimate nutrient concentration.
- **pH Sensor**: Monitors pH levels to maintain optimal acidity for plants.
- **Temperature Sensor**: Tracks temperature as it affects nutrient uptake.
- **LEDs**: Indicates nutrient balance status; green for balanced, red for imbalanced.
- **Display Screen (LCD/LED)**: Shows sensor readings and alerts in real time.

---

## Project Demo

https://github.com/user-attachments/assets/16ed94bb-71a6-4895-9140-bfa0b4d7f15c


---

## How It Works
1. **User Input**: Users select the plant type via the serial interface, choosing from preset options (lettuce, tomatoes, spinach, basil, peppers, and cucumbers).
2. **Sensor Readings**: The system reads raw values from the EC, pH, and temperature sensors.
3. **Data Processing**:
   - Sensor values are converted to voltages.
   - Calculations for EC, pH, and temperature are done based on the voltage readings.
4. **Balance Check**:
   - The system evaluates nutrient balance based on the sensor values.
   - If the parameters fall within the optimal range for the selected plant, it shows "Nutrient balance: Balanced" and activates the green LED.
   - If the readings indicate an imbalance, it shows "Nutrient balance: Imbalanced," triggers the red LED, and provides recommendations.
5. **Display Output**:
   - Sensor readings and nutrient balance status are displayed on an LED screen for easy monitoring.

### Example Workflow:
- **Input**: Select "Spinach" from the plant menu.
- **Reading Output**:
  ```
  Select Plant:
  0: Lettuce
  1: Tomatoes
  2: Spinach
  3: Basil
  4: Peppers
  5: Cucumbers
  Enter plant index (0-5): Selected Plant: Spinach
  Raw EC Value: 0
  Raw pH Value: 0
  Raw Temperature Value: 1023
  EC Voltage: 0.00
  pH Voltage: 0.00
  Temperature Voltage: 5.00
  EC: -5.00
  pH: 0.00
  Temperature: 450.0
  Nutrient balance: Balanced
  Press any key to check another plant.
  Select Plant:
  0: Lettuce
  1: Tomatoes
  2: Spinach
  3: Basil
  4: Peppers
  5: Cucumbers
  Enter plant index (0-5): Selected Plant: Cucumbers
  Raw EC Value: 0
  Raw pH Value: 0
  Raw Temperature Value: 1023
  EC Voltage: 0.00
  pH Voltage: 0.00
  Temperature Voltage: 5.00
  EC: -5.00
  pH: 0.00
  Temperature: 450.0
  Nutrient balance: Imbalanced
  Recommendation: Increase nutrients and temperature
  Press any key to check another plant.
  ```

### System Messages
- **Balanced**: "Nutrient balance: Balanced" and green LED.
- **Imbalanced**: "Nutrient balance: Imbalanced" and red LED with recommendations.

---

## Setup and Installation
### Hardware Assembly
1. Connect the EC, pH, and temperature sensors to the respective analog pins on the Arduino.
2. Attach the green and red LEDs to digital pins, with appropriate resistors.
3. Set up the LED/LCD screen to display sensor readings and messages.

### Software Setup
1. Download and install the Arduino IDE.
2. Clone this repository to your local machine:
   ```bash
   https://github.com/Soumyakc-161/Nutrient-Management-System-IoT-Project
   ```
3. Open the Arduino sketch file `NutrientManagementSystem`.
4. Verify and upload the code to your Arduino board.

---

## Code Explanation
The core functionality is organized as follows:

- **Plant Selection**: Prompts user to select a plant, sets the optimal nutrient parameters.
- **Data Collection**: Reads raw sensor values (EC, pH, temperature).
- **Data Conversion**: Converts raw sensor values to voltage and meaningful units (e.g., pH scale, EC units).
- **Balance Check & Alert**:
  - Checks if readings are within optimal limits for the selected plant.
  - If balanced, lights the green LED; if imbalanced, lights the red LED and displays corrective action.
- **Display Output**: Shows plant selection, sensor readings, and status on the LED/LCD.

### Example Code Snippet:
```cpp
int plantIndex;
Serial.println("Enter plant index (0-5): ");
plantIndex = Serial.parseInt();

if (plantIndex >= 0 && plantIndex <= 5) {
    displaySelectedPlant(plantIndex);
    readSensorValues();
    checkBalanceAndDisplayAlert();
}
```

---

## Usage
1. Power the Arduino and open the serial monitor.
2. Follow the prompts to select a plant type.
3. View real-time sensor readings and status alerts.
4. Adjust nutrients based on recommendations if any imbalances are detected.

---

## Troubleshooting
- **Sensor Not Reading**: Ensure proper connection and calibration.
- **Incorrect Readings**: Check sensor calibration, especially for pH and EC.
- **No Display Output**: Verify LED/LCD connections and code for display output.

---

## Future Enhancements
- Adding a mobile app interface for remote monitoring.
- Integrating automated nutrient adjustment based on sensor feedback.
- Implementing additional sensors for other environmental factors (e.g., humidity, CO2).

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.

--- 

## Contribution
Feel free to open issues or submit pull requests for improvements. Contributions are welcome!

Soumya.kc02@gmail.com

