#!/usr/bin/env python

import time

from envirophat import weather, leds


print("""This example will detect temperature using the onboard sensor 

Press Ctrl+C to exit.

""")

threshold = None

try:
    while True:
        temperature = weather.temperature()

        if threshold is None:
            threshold = temperature + 2

        print("{} degrees celcius".format(temperature))
        if temperature > threshold:
            leds.on()
        else:
            leds.off()

        time.sleep(0.1)

except KeyboardInterrupt:
    pass
