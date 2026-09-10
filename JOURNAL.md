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
const int mq2Pin = 34; // Nakakonekta ang AO sa D34

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
