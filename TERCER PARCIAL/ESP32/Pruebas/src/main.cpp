#include <Arduino.h>

#include <Adafruit_ST7735.h>  // Hardware-specific library for ST7735
#include <SPI.h>

//Coneccion de la pantalla
// tft display | ESP32-S3 N16
// GND         | GND
// VCC         | 3V3
// SCL         | IO18
// SDA         | IO23
// RES         | IO4
// DC          | IO2
// CS          | IO5


#define TFT_CS 10
#define TFT_DC 8
#define TFT_RST 9
#include <SPI.h>
#include "Adafruit_GFX.h"
#include "Adafruit_GC9106_kbv.h"
Adafruit_GC9106_kbv tft(TFT_CS, TFT_DC, TFT_RST);