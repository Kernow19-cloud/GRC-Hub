import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogHandler(FileSystemEventHandler):
    """Handle log file changes (PCI-DSS Requirement 10)."""
    def on_modified(self, event):
        if not event.is_directory:
            logging.info(f"Log file modified: {event.src_path}")

def monitor_logs(log_path="/var/log/access.log"):
    """Monitor access logs for changes."""
    observer = Observer()
    event_handler = LogHandler()
    observer.schedule(event_handler, log_path, recursive=False)
    observer.start()
    logging.info(f"Monitoring log file: {log_path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_logs()
