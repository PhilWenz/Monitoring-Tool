from abc import ABC, abstractmethod
import logging


class Alarm:

    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL}
    level: int

    def parse_level(self, level):
        try:
            return int(level)
        except ValueError:
            # Level wurde als String übergeben
            return self.levels[level]

    @abstractmethod
    def log(self, level, message, value, soft_threshold=None, hard_threshold=None):
        print("Abstrakte Methode, bitte überschreiben")

