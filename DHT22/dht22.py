import time
import adafruit_dht
import board

dht_device = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        print("Temp:{:.1f}  |  Humidity: {}%".format(temperature_c, humidity))
    except RuntimeError as err:
        print(err.args[0])

    time.sleep(5.0)