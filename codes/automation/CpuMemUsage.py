import psutil
import time
import logging

# Configure logging
logging.basicConfig(
    filename='system_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',  # Correctly using 'asctime'
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Monitoring interval in seconds
interval = 60

interactions = 3

for i in range(interactions):
    # Get CPU usage
    cpu_percent = psutil.cpu_percent()

    # Get memory usage
    memory = psutil.virtual_memory()
    memory_percent = memory.percent

    # Log the information
    logging.info(f"CPU Usage: {cpu_percent}%")
    logging.info(f"Memory Usage: {memory_percent}%")

    # Wait for the specified interval
    time.sleep(interval)
