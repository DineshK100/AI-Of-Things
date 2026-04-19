import RPi.GPIO as GPIO
import time

PIR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print("Ready! Watching for motion (Ctrl+C to stop)\n")

try:
    while True:
        if GPIO.input(PIR_PIN):
            time.sleep(0.5)  # wait and check again
            if GPIO.input(PIR_PIN):  # still HIGH? then real motion
                print("Motion detected!")
                time.sleep(1)
        else:
            print("No motion...")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nStopped.")
    GPIO.cleanup()
