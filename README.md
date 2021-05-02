# bfaulty
My project as part of [#growlab](https://blog.alexellis.io/the-grow-lab-challenge/), set up by Alex Ellis as a global communty to grow and monitor your own food with the Raspberry Pi.

Note that this a fork of Alex's original [#growlab](https://github.com/alexellis/growlab) repo, customized for my own hardware.

## Hardware

I used the following for my growlab. This is mostly due to what parts I had on hand, Alex has a much lighterweight, cleaner and less expensive solution in his [repo](https://github.com/alexellis/growlab).

 - Raspberry Pi Zero WH  ([UK](https://amzn.to/33rmXEc), [US](https://amzn.to/3lcQLul))
 - Micro SD Card  ([UK](https://amzn.to/2SoRagP), [US](https://amzn.to/2GeMWWT))
 - BME280 - Off-board digital temperature, pressure & humidity sensor I2C ([UK](https://amzn.to/335du4n), [US]() )
 - Soil Moisture Sensor Hygrometer Module (Capacitive) ([UK](https://amzn.to/2Rf93Bu), [US]() )
 - Sense HAT B. Onboard Gyroscope, Accelerometer, Magnetometer, Barometer, Temperature and Humidity Sensor, I2C Interface. ([UK](https://amzn.to/2Rg2kqX), [US]() )
 - Raspberry Pi High quality Camera  ([Pimoroni](https://shop.pimoroni.com/products/raspberry-pi-high-quality-camera) )
 - Raspberry Pi High quality Camera  ([Pimoroni](https://shop.pimoroni.com/products/raspberry-pi-high-quality-camera) )
 - Wide angle lens for HQ Camera ([Pimoroni](https://shop.pimoroni.com/products/raspberry-pi-hq-camera-lens?variant=31675768995923) )
 - 30cm Raspberry Pi Zero Camera Cable (15pin to 22pin) ([UK](https://amzn.to/3xJgMZd), [US]() )
 - USB power - I have a 3m USB cable into a all socket, but you can also power with a USB battery pack. Be sure to provide 2.1A to help power the camera etc.
 - Sheet of 1mm thick aluminium (cut to size)
 - M2.5 hardware to attach to aluminium sheet ([UK](), [US]() )
 - Plastic tray, compost & horticultural grit

Note the Sense HAT B was overkill for this project, but I had it handy when I started.  The onboard temperature sensor turned out to be less than useful as when installed picks up heat from the Raspberry Pi Zero. However it contained an analog to digital convertor which was helpful for the capacitive soil sensor and and handy plug for the i2c interface to attach to an external BME280 sensor I purchased and attached to the aluminum sheet via an M2.5 metal screw and couple of metal bolts to help get the correct ambient temperature new the growing plant.  I also use the onboard color sensor to detect ambient light levels.





