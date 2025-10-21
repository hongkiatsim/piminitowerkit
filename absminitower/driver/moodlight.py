import time
from rpi_ws281x import PixelStrip, Color
import logging

logger = logging.getLogger(__name__)

class MoodLight:
    def __init__(self, pin, count):
        self.strip = PixelStrip(count, int(pin))
        self.strip.begin()
        logger.info(f"MoodLight initialized on pin {pin} with {count} LEDs")

    def rainbow_cycle(self, wait_ms=20, iterations=5):
        """Cycle colors across all LEDs."""
        for j in range(256 * iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self.wheel((i + j) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def wheel(self, pos):
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        if pos < 170:
            pos -= 85
            return Color(255 - pos *3, 0, pos *3)
        pos -= 170
        return Color(0, pos *3, 255 - pos *3)

    def set_color(self, r, g, b):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(r, g, b))
        self.strip.show()
