class MonitoringData:
    values: dict
    messages: dict
    soft_threshold: float
    hard_threshold: float
    log_level = "INFO"

    def __init__(self, values: dict, messages: dict, soft_threshold: float = None, hard_threshold: float = None, log_level=None) -> None:
        self.values = values
        self.messages = messages
        self.soft_threshold = soft_threshold
        self.hard_threshold = hard_threshold
        if log_level is not None:
            self.log_level = log_level

    def testPrinter(self):
        dict_values = self.values.items()
        for value in dict_values:
            print(value)
        dict_messanges = self.messages.items()
        for msg in dict_messanges:
            print(msg)
        print(self.soft_threshold)
        print(self.hard_threshold)
