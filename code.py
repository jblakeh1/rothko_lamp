import time
import array
import math
import board
import audiobusio
import neopixel
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.2

# -------------------------------------------------------------------
# mic functions
# -------------------------------------------------------------------
def constrain(value, floor, ceiling):
    return max(floor, min(value, ceiling))

def log_scale(input_value, input_min, input_max, output_min, output_max):
    normalized_input_value = (input_value - input_min) / (input_max - input_min)
    return output_min + math.pow(normalized_input_value, 0.630957) * (
        output_max - output_min
    )

def normalized_rms(values):
    minbuf = int(sum(values) / len(values))
    return math.sqrt(
        sum(float(sample - minbuf) * (sample - minbuf) for sample in values)
        / len(values)
    )

mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate=16000, bit_depth=16
)

samples = array.array("H", [0] * 160)
mic.record(samples, len(samples))
input_floor = normalized_rms(samples) + 10

# Lower number means more sensitive - more LEDs will light up with less sound.
sensitivity = 1000
input_ceiling = input_floor + sensitivity

peak = 0

# -------------------------------------------------------------------
# light sensor
# -------------------------------------------------------------------
def scale_range(value):
    """Scale a value from 0-320 (light range) to 0-9 (NeoPixel range).
    Allows remapping light value to pixel position."""
    return round(value / 320 * 9)

# -------------------------------------------------------------------
# neopixel strip
# -------------------------------------------------------------------
NUMPIXELS = 60  # Update this to match the number of LEDs.
BRIGHTNESS = 0.6  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.A7  # This is the default pin on the 5x5 NeoPixel Grid BFF.
pixel_strip = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)

# -------------------------------------------------------------------
# colors
# -------------------------------------------------------------------
BLACK = (0, 0, 0)

SHERBET = (127, 20, 0)
SALMON = (80, 0, 20)
MAGENTA = (127, 0, 80)
POMENGRANITE = (127, 0, 2)
POMENGRANITE2 = (208, 8, 8)
LEMON = (127, 80, 0)

PERIWINKLE = (2, 0, 80)
PERIWINKLE2 = (40, 0, 127)
AQUA = (0, 80, 20)
MARINE = (0, 80, 40)
MIDNIGHT = (20, 0, 127)
LIME = (20, 127, 0)

WARM_COLORS = [SALMON, SHERBET, POMENGRANITE, LEMON, POMENGRANITE2, LEMON, SALMON, SHERBET, LEMON, POMENGRANITE, SALMON, SHERBET, POMENGRANITE]
COOL_COLORS = [MIDNIGHT, AQUA, PERIWINKLE, MARINE, MIDNIGHT, AQUA, PERIWINKLE, MARINE, LIME, PERIWINKLE, MARINE, LIME]

while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)

    c = log_scale(
        constrain(magnitude, input_floor, input_ceiling),
        input_floor,
        input_ceiling,
        0,
        9,
    )
    
    d = scale_range(cp.light)

    x = int((c + d)/2)
    y = x + 1

    for i in range(0, 5):
        cp.pixels[i] = WARM_COLORS[x]
        cp.pixels.show()
        time.sleep(0.1)

    for i in range(5, 10):
        cp.pixels[i] = COOL_COLORS[x]
        cp.pixels.show()
        time.sleep(0.1)

    for i in range(0, 30):
        pixel_strip[i] = WARM_COLORS[x]
        pixel_strip.show()
        time.sleep(0.1)

    for i in range(30, 60):
        pixel_strip[i] = COOL_COLORS[x]
        pixel_strip.show()
        time.sleep(0.1)

    for i in range(0, 5):
        cp.pixels[i] = WARM_COLORS[y]
        cp.pixels.show()
        time.sleep(0.1)

    for i in range(5, 10):
        cp.pixels[i] = COOL_COLORS[y]
        cp.pixels.show()
        time.sleep(0.1)
        
    for i in range(0, 30):
        pixel_strip[i] = WARM_COLORS[y]
        pixel_strip.show()
        time.sleep(0.1)

    for i in range(30, 60):
        pixel_strip[i] = COOL_COLORS[y]
        pixel_strip.show()
        time.sleep(0.1)
