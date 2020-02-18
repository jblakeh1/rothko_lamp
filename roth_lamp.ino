// testshapes demo for Adafruit RGBmatrixPanel library.
// Demonstrates the drawing abilities of the RGBmatrixPanel library.
// For 32x32 RGB LED matrix:
// http://www.adafruit.com/products/607

// Written by Limor Fried/Ladyada & Phil Burgess/PaintYourDragon
// for Adafruit Industries.
// BSD license, all text above must be included in any redistribution.

#include <RGBmatrixPanel.h>

// Most of the signal pins are configurable, but the CLK pin has some
// special constraints.  On 8-bit AVR boards it must be on PORTB...
// Pin 8 works on the Arduino Uno & compatibles (e.g. Adafruit Metro),
// Pin 11 works on the Arduino Mega.  On 32-bit SAMD boards it must be
// on the same PORT as the RGB data pins (D2-D7)...
// Pin 8 works on the Adafruit Metro M0 or Arduino Zero,
// Pin A4 works on the Adafruit Metro M4 (if using the Adafruit RGB
// Matrix Shield, cut trace between CLK pads and run a wire to A4).

#define CLK  8   // USE THIS ON ARDUINO UNO, ADAFRUIT METRO M0, etc.
//#define CLK A4 // USE THIS ON METRO M4 (not M0)
//#define CLK 11 // USE THIS ON ARDUINO MEGA
#define OE   9
#define LAT 10
#define A   A0
#define B   A1
#define C   A2
#define D   A3

RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false);

uint16_t lemon = matrix.Color333(7, 4, 0);
uint16_t sherbet = matrix.Color333(7, 2, 0);
uint16_t salmon = matrix.Color333(6, 1, 1);
uint16_t magenta = matrix.Color333(7, 0, 2);
uint16_t rose = matrix.Color333(6, 0, 4);
uint16_t violet = matrix.Color333(4, 0, 6);
uint16_t periwinkle = matrix.Color333(1, 0, 7);
uint16_t sky = matrix.Color333(1, 4, 6);
uint16_t aqua = matrix.Color333(0, 7, 2);
uint16_t lime = matrix.Color333(26, 6, 0);

uint16_t colors[] = {lemon, sherbet, salmon, magenta, rose, violet, periwinkle, sky, aqua, lime, lemon, sherbet, salmon, magenta, rose, violet, periwinkle, sky, aqua, lime};

void setup() {
  matrix.begin();
  matrix.fillScreen(matrix.Color333(0, 0, 0));
  matrix.setTextSize(1);
  
//   shapes
//   matrix.drawPixel(0, 0, matrix.Color333(7, 7, 7));
//   matrix.drawRect(0, 0, 32, 32, matrix.Color333(7, 7, 0));
//   matrix.fillRect(0, 0, 32, 32, colors[0]);
//   matrix.drawLine(0, 0, 31, 31, matrix.Color333(7, 0, 0));
//   matrix.drawCircle(10, 10, 10, matrix.Color333(0, 0, 7));
//   matrix.fillCircle(21, 21, 10, matrix.Color333(7, 0, 7));

//   text
//   matrix.setCursor(1, 0);    // start at top left, with one pixel of spacing
//   matrix.setTextSize(0);     // size 1 == 8 pixels high
//   matrix.setTextWrap(false); // Don't wrap at end of line - will do ourselves
//   matrix.println(" Ada");
//   matrix.setTextColor(matrix.Color333(0,7,7));
//   matrix.print('R');
}

void loop() {
  int sensorValue = analogRead(A5);
    int valueRounded = sensorValue/100;

    if (valueRounded < 1) {
        matrix.fillScreen(matrix.Color333(0, 0, 0));
    } 
    else {
    matrix.fillRect(0, 2, 32, 15, colors[valueRounded]);
    matrix.fillRect(0, 17, 32, 16, colors[valueRounded + 2]);
    matrix.fillRect(0, 0, 32, 2, colors[valueRounded + 6]);
    }
  delay(500);

}
