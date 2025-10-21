#!/usr/bin/env bash
set -e

# Read configuration from environment or file
MQTT_BROKER="${MQTT_BROKER:-${mqtt_broker}}"
MQTT_TOPIC="${MQTT_TOPIC:-${mqtt_topic}}"
OLED_BUS="${OLED_I2C_BUS:-${oled_i2c_bus}}"
OLED_ADDR="${OLED_I2C_ADDR:-${oled_i2c_addr}}"
LED_PIN="${LED_DATA_PIN:-${led_data_pin}}"
LED_COUNT="${LED_COUNT:-${led_count}}"

# Export or pass into the Python driver
export MQTT_BROKER MQTT_TOPIC OLED_BUS OLED_ADDR LED_PIN LED_COUNT

echo "Starting ABS Mini Tower Kit driver..."
python3 -u driver/main.py
