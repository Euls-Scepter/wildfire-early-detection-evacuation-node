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

---

## 7. Uploading the Program

I uploaded the test program to the ESP32 using Arduino IDE.

The upload was completed successfully.

The Arduino IDE output showed:

Writing at 0x0004efc0 [==============================] 100.0%

Wrote 257984 bytes (147862 compressed) at 0x00010000

Verifying written data...

Hash of data verified.

Hard resetting via RTS pin...

The successful verification confirmed that the program was correctly written to the ESP32's flash memory.

---

## 8. Final Hardware Test

After uploading the program, the ESP32 automatically restarted.

The onboard blue LED started blinking repeatedly, following the programmed one-second ON and one-second OFF pattern.

This confirmed that the ESP32 was not only receiving power and communicating with the computer, but was also successfully executing the uploaded program.

Final Result
| Test                         | Result      |
| ---------------------------- | ----------- |
| ESP32 receives power         | PASS        |
| Power LED                    | PASS        |
| CP2102 USB-to-UART detection | PASS        |
| CP210x driver installation   | PASS        |
| COM port detection           | PASS – COM3 |
| Arduino IDE connection       | PASS        |
| ESP32 board package          | PASS        |
| Program compilation          | PASS        |
| Program upload               | PASS        |
| Flash verification           | PASS        |
| ESP32 program execution      | PASS        |
| Onboard LED test             | PASS        |

Conclusion

The initial hardware test of the ESP32 was successful.

The board was able to receive power, communicate with the laptop through the CP2102 USB-to-UART interface, appear as COM3, receive a program from Arduino IDE, verify the uploaded firmware, restart, and execute the LED blinking program.

Based on these tests, the ESP32 is currently functioning properly and can proceed to the next stage of the project.

The next step is to test the project's sensors individually, starting with the MQ-2 gas sensor and TMP36 temperature sensor, before integrating them into the Wildfire Early-Detection & Evacuation Node.


