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
