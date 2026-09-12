# ESP32 Hardware Testing Journal

## Project
**Wildfire Early-Detection & Evacuation Node**

## Date
September 10, 2026

---

## Day 1 – ESP32 Hardware Setup and Initial Testing

### Objective

The objective of this activity was to verify whether the ESP32 development board was functioning properly before connecting the sensors and other components for the Wildfire Early-Detection & Evacuation Node project.

The ESP32 was tested first as a standalone development board to make sure that the USB connection, USB-to-UART communication, drivers, board configuration, and program uploading were working correctly.

---

## 1. Connecting the ESP32

I connected the ESP32 development board to my Windows laptop using a Micro-USB cable.

After connecting the board, the red power LED turned on. This indicated that the ESP32 was receiving power from the laptop.

### Initial Observation

- ESP32 received power: **YES**
- Red power LED: **ON**
- USB connection: **Detected**

---

## 2. Checking the ESP32 in Device Manager

I opened Windows Device Manager to check whether the ESP32 was properly detected.

The USB-to-UART controller appeared as:

**CP2102 USB to UART Bridge Controller**

However, Windows initially displayed a yellow warning icon because the required driver was not installed.

The device properties showed:

> The drivers for this device are not installed. (Code 28)

This indicated that the problem was related to the missing CP210x driver rather than an immediate indication that the ESP32 board was defective.

---

## 3. Installing the CP210x Driver

I downloaded and installed the **CP210x Universal Windows Driver** from Silicon Labs.

After installation, Windows successfully recognized the USB-to-UART bridge.

The ESP32 was then assigned to:

**COM3**

### Result

- CP210x driver: **Installed**
- USB-to-UART communication: **Working**
- Serial Port: **COM3**

---

## 4. Installing Arduino IDE

I installed **Arduino IDE 2.3.10** on the Windows laptop.

Arduino IDE was used because it provides the tools needed to compile and upload programs to the ESP32.

---

## 5. Installing ESP32 Board Support

The ESP32 board package was installed through the Arduino IDE Boards Manager.

The package installed was:

**esp32 by Espressif Systems**

Installed version:

**3.3.11**

After installation, I selected:

**ESP32 Dev Module**

as the board configuration.

The port was configured to:

**COM3**

---

## 6. Creating the ESP32 Test Program

To verify that the ESP32 could execute a program, I created a simple LED blinking program.

```cpp
#define LED_PIN 2

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  delay(1000);

  digitalWrite(LED_PIN, LOW);
  delay(1000);
}
```

---

## Date
September 11, 2026

---

## Day 2 – MQ-2 Gas Sensor Testing and Calibration

### Objective

The objective of this activity was to test and verify the functionality of the MQ-2 gas sensor module using the ESP32 development board to ensure it is fully operational and capable of detecting smoke or flammable gases.

---

## 1. Connecting the MQ-2 Sensor

I connected the MQ-2 gas sensor module to the ESP32 using Female-to-Female (F-F) DuPont jumper wires.

- VCC to **VIN**
- GND to **GND**
- AO to **D34** (GPIO 34)

### Initial Observation

- MQ-2 powered on: **YES**
- Wiring configuration: **Completed**
- Analog pin assigned: **D34**

---

## 2. Configuring the Arduino IDE Serial Monitor

To properly read the analog output data from the sensor without getting garbled or square characters, I set the baud rate in the Arduino IDE Serial Monitor to match the program configuration.

### Configuration Details

- Baud Rate: **115200**
- Port: **COM3**

---

## 3. Creating the MQ-2 Test Program

To verify that the ESP32 could read analog data from the MQ-2 sensor, I created and uploaded a monitoring program.

```cpp
const int mq2Pin = 34; // AO connected to D34

void setup() {
  Serial.begin(115200);
  delay(1000);
}

void loop() {
  int sensorValue = analogRead(mq2Pin);
  Serial.print("MQ-2 Value: ");
  Serial.println(sensorValue);
  delay(1000);
}
```

---

---

## Date
September 12, 2026

---

## Day 3 – TMP36 Temperature Sensor Testing and Calibration

### Objective

The objective of this activity was to test and verify the functionality of the TMP36 temperature sensor using the ESP32. The sensor was tested to determine whether it could provide temperature readings through its analog output and respond appropriately to changes in temperature.

---

## 1. Connecting the TMP36 Sensor

I connected the TMP36 temperature sensor to the ESP32 using Female-to-Female (F-F) DuPont jumper wires and a breadboard for the common ground connection.

The connections were configured as follows:

- **+Vs → ESP32 3V3**
- **Vout → ESP32 GPIO35 (D35)**
- **GND → Breadboard negative (-) rail**
- **ESP32 GND → Breadboard negative (-) rail**

GPIO35 was used as the analog input for reading the TMP36 output voltage.

### Initial Observation

- TMP36 powered: **YES**
- TMP36 analog output: **Detected**
- Analog input pin: **GPIO35**
- Common ground connection: **Completed**

---

## 2. Creating the Combined MQ-2 and TMP36 Test Program

The MQ-2 and TMP36 were tested together using the ESP32.

The TMP36 was configured using the ESP32 ADC with 0 dB attenuation because its output voltage is relatively low.

```cpp
const int mq2Pin = 34;
const int tmp36Pin = 35;

void setup() {
  Serial.begin(115200);
  delay(1000);

  analogSetPinAttenuation(tmp36Pin, ADC_0db);

  Serial.println("Wildfire Detection Node");
  Serial.println("MQ-2 + TMP36 Calibrated Test");
  Serial.println("--------------------------------");
}

void loop() {
  int mq2Value = analogRead(mq2Pin);

  int tmp36Raw = analogRead(tmp36Pin);

  uint32_t tmp36mV = analogReadMilliVolts(tmp36Pin);

  float tmp36Voltage = tmp36mV / 1000.0;

  float temperatureC = (tmp36mV - 500) / 10.0;

  Serial.print("MQ-2 Value: ");
  Serial.print(mq2Value);

  Serial.print(" | TMP36 Raw: ");
  Serial.print(tmp36Raw);

  Serial.print(" | TMP36 Voltage: ");
  Serial.print(tmp36Voltage, 3);
  Serial.print(" V");

  Serial.print(" | Temperature: ");
  Serial.print(temperatureC, 2);
  Serial.println(" °C");

  delay(1000);
}

```
---

## 3. Indoor Testing

The TMP36 was initially tested inside the room under normal indoor conditions.

The Serial Monitor produced temperature readings generally within the range of approximately **28°C to 33°C**.

Example readings included:

```text
TMP36 Voltage: 0.790 V | Temperature: 29.0 °C
TMP36 Voltage: 0.806 V | Temperature: 30.6 °C
TMP36 Voltage: 0.834 V | Temperature: 33.4 °C
TMP36 Voltage: 0.820 V | Temperature: 32.0 °C
TMP36 Voltage: 0.783 V | Temperature: 28.3 °C
TMP36 Voltage: 0.811 V | Temperature: 31.1 °C
```

The readings demonstrated that the TMP36 was producing measurable analog voltage and that the ESP32 was successfully converting the sensor output into temperature values.

---

## 4. Hand-Warming Test

A hand-warming test was performed to verify whether the TMP36 would respond to an increase in temperature.

The sensor was warmed by holding it with the hand. During the test, the temperature reading increased and reached approximately 40°C.

The readings were not completely consistent because the sensor temperature changed depending on hand contact, heat transfer, airflow, and the surrounding environment.

The important observation was that the temperature reading increased when the sensor was warmed and gradually decreased when the sensor was released.

Result
Response to hand warming: Detected
Temperature increase: Observed
Sensor response: Working

---

## 5. Outdoor Warming Test

The TMP36 was also tested outside the house. The sensor was exposed to the warmer outdoor environment for several seconds.

The following readings were observed:
```text
TMP36 Voltage: 0.723 V | Temperature: 22.3 °C
TMP36 Voltage: 0.821 V | Temperature: 32.1 °C
TMP36 Voltage: 0.847 V | Temperature: 34.7 °C
TMP36 Voltage: 0.874 V | Temperature: 37.4 °C
TMP36 Voltage: 0.895 V | Temperature: 39.5 °C
TMP36 Voltage: 1.008 V | Temperature: 50.8 °C
```

The readings increased as the sensor was exposed to heat.

The approximately 50.8°C reading was considered a heat-response result rather than an exact measurement of the surrounding air temperature because direct environmental heating can cause the sensor itself to become warmer than the actual ambient air.

---

## 6. TMP36 Temperature Conversion

The TMP36 temperature was calculated using the standard voltage-to-temperature relationship:
Temperature (°C) = (Voltage - 0.500) × 100

For example:
Voltage = 0.790 V

Temperature = (0.790 - 0.500) × 100
Temperature = 29.0 °C

This confirmed that the voltage readings were being converted into temperature values correctly.

---

## 7. TMP36 Testing Result

The TMP36 successfully produced analog readings through GPIO35 and responded to changes in temperature.

The sensor demonstrated the expected behavior during indoor, hand-warming, and outdoor warming tests.

Result
TMP36 powered: YES
Analog output detected: YES
ESP32 GPIO35 reading: Working
Voltage measurement: Working
Temperature conversion: Working
Response to hand warming: Detected
Response to outdoor heat: Detected
TMP36 hardware test: PASSED
