import logging
import datetime


class Logger:
    log_dir = f"source/logs/daitex_software_test_task, {datetime.datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}"

    def get_logger(self):
        logger = logging.getLogger(__name__)
        file_handler = logging.FileHandler(self.log_dir)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        return logger
