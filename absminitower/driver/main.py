import os
import logging
import time
import paho.mqtt.client as mqtt

from moodlight import MoodLight
from oled_display import OLEDDisplay

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("absminitowerkit")

def main():
    # Read config from env
    mqtt_broker = os.getenv("MQTT_BROKER", "core-mosquitto")
    mqtt_topic = os.getenv("MQTT_TOPIC", "absminitowerkit")
    oled_bus = os.getenv("OLED_BUS", "1")
    oled_addr = os.getenv("OLED_ADDR", "0x3C")
    led_pin = os.getenv("LED_PIN", "18")
    led_count = int(os.getenv("LED_COUNT", "30"))

    logger.info(f"Connecting to MQTT broker {mqtt_broker} on topic {mqtt_topic}")
    client = mqtt.Client()
    client.connect(mqtt_broker)
    client.loop_start()

    oled = OLEDDisplay(oled_bus, oled_addr)
    mood = MoodLight(led_pin, led_count)

    try:
        while True:
            # publish some state
            cpu = os.getloadavg()[0]
            client.publish(f"{mqtt_topic}/cpu", cpu)
            # update display
            oled.loop(interval=10)
            # run mood light rainbow effect
            mood.rainbow_cycle(iterations=1)
    except KeyboardInterrupt:
        logger.info("Stopping driver")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
