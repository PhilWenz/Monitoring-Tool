from alarm import AlarmFactory
from monitoring_data import MonitoringData


class AlarmModule:

    log_file_url: str
    log_level: str

    def __init__(self, log_file_url: str, log_level: str):
        self.log_file_url = log_file_url
        self.log_level = log_level

    def log(self, data: MonitoringData, log_level=None):
        values: dict = data.values
        messages: dict = data.messages
        soft_threshold = data.soft_threshold
        hard_threshold = data.hard_threshold
        if data.log_level is not None:
            log_level = data.log_level

        # Testen ob es Werte zu prüfen gibt oder nur Nachrichten zu loggen
        if len(values.keys()) == 0:
            if len(messages.keys()) != 0:
                for message in messages.keys():
                    self.output(log_level=log_level, message=messages[message])
            else:
                return

        else:
            for label in values:
                value = None
                try:
                    value = float(values[label])
                except TypeError as e:
                    self.output(log_level="ERROR", message="Der angegebene Wert ist keine Fließkommazahl.")

                # Wenn keine Message zum Label existiert wird einfach der Wert und das Label als Nachricht ausgegeben
                message = f"{label}: {values[label]}"
                if label in messages.keys():
                    message = messages[label]

                self.output(log_level=log_level, message=message, value=value, soft_threshold=soft_threshold, hard_threshold=hard_threshold)

    def output(self, log_level=None, message=None, value: float = None, soft_threshold=None, hard_threshold=None):
        if log_level is None:
            log_level = self.log_level
        af = AlarmFactory(logfile_url=self.log_file_url, level=log_level)\
            .get_alarm(value, soft_threshold, hard_threshold)\
            .log(level=log_level, message=message, value=value, soft_threshold=soft_threshold, hard_threshold=hard_threshold)
