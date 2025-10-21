import logging
import time
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont
from utils import cpu_usage, memory_usage, uptime

logger = logging.getLogger(__name__)

class OLEDDisplay:
    def __init__(self, i2c_bus, i2c_addr):
        serial = i2c(device=i2c_bus, address=int(i2c_addr, 16))
        self.device = ssd1306(serial)
        self.font = ImageFont.load_default()
        logger.info(f"OLEDDisplay initialized on I2C bus {i2c_bus}, address {i2c_addr}")

    def show_stats(self):
        with Image.new("1", (self.device.width, self.device.height)) as image:
            draw = ImageDraw.Draw(image)
            draw.text((0, 0), f"CPU: {cpu_usage():5.1f}%", font=self.font, fill=255)
            draw.text((0, 10), f"Mem: {memory_usage():5.1f}%", font=self.font, fill=255)
            uptime_h = uptime() / 3600
            draw.text((0, 20), f"Up: {uptime_h:5.1f}h", font=self.font, fill=255)
            self.device.display(image)

    def loop(self, interval=5):
        while True:
            self.show_stats()
            time.sleep(interval)
