from alarm import LogAlarm, EmailAlarm


class AlarmFactory:
    logfile_url: str
    level: str

    def __init__(self, logfile_url: str, level: str):
        self.logfile_url = logfile_url
        self.level = level

    def get_alarm(self, value, soft_threshold=None, hard_threshold=None):
        new_alarm = LogAlarm(self.logfile_url, self.level)
        if value is None or soft_threshold is None or hard_threshold is None:
            return new_alarm
        else:
            return EmailAlarm(new_alarm)
