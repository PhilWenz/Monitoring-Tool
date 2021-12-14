import logging
from alarm import Alarm
import datetime


class LogAlarm(Alarm):

    logfile_url: str
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    def __init__(self, logfile_url: str, level) -> None:
        self.logfile_url = logfile_url
        self.level = self.parse_level(level)
        logging.basicConfig(filename=logfile_url, level=logging.DEBUG)
        pass

    def log(self, message: str, value=None, level=None, soft_threshold=None, hard_threshold=None):
        if value is not None and soft_threshold is not None:
            if value >= soft_threshold:
                level = self.WARNING

        if level is None:
            level = "INFO"
        else:
            level = self.parse_level(level)

        if level >= self.level:
            print(f'{logging.getLevelName(level)}:{logging.getLogger().name}:{message}')
            message = datetime.datetime.now().strftime("%d%m%Y%H%M%S:") + message
        logging.log(level, message)

