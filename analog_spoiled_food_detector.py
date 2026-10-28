import spidev
import RPi.GPIO as GPIO
import time

# Analog-Based Spoiled Food Detection Indicator
# Hardware: Raspberry Pi + MCP3008 ADC + MQ gas sensor
# NOTE: Calibrate THRESHOLD for your sensor and test conditions.
# This indicates a gas threshold, not food safety itself.

GREEN_LED = 17
RED_LED = 27
BUZZER = 22
THRESHOLD = 400

GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

def read_sensor():
    data = spi.xfer2([1, 0x80, 0])
    return ((data[1] & 3) << 8) | data[2]

try:
    while True:
        gas_value = read_sensor()
        print("Gas Sensor Value:", gas_value)

        if gas_value > THRESHOLD:
            print("Warning: Possible food spoilage!")
            GPIO.output(GREEN_LED, GPIO.LOW)
            GPIO.output(RED_LED, GPIO.HIGH)
            GPIO.output(BUZZER, GPIO.HIGH)
        else:
            print("No spoilage threshold exceeded.")
            GPIO.output(GREEN_LED, GPIO.HIGH)
            GPIO.output(RED_LED, GPIO.LOW)
            GPIO.output(BUZZER, GPIO.LOW)

        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped.")

finally:
    spi.close()
    GPIO.cleanup()
