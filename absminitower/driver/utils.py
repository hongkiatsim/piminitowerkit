import time
import logging
import psutil

logger = logging.getLogger(__name__)

def cpu_usage():
    return psutil.cpu_percent(interval=1)

def memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent

def uptime():
    return time.time() - psutil.boot_time()
