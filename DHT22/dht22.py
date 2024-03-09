import adafruit_dht
from board import D17

dht_device = adafruit_dht.DHT22(D17)

temperature = dht_device.temperature
humidity = dht_device.humidity
print("temperature: ", temperature)
print("humidity: ", humidity)

