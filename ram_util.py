import psutil
from monitoring_data import MonitoringData


class RamUtil:

    # gibt einen Prozentsatz des genutzen Rams zurück
    @staticmethod
    def ramused(config) -> MonitoringData:
        psutool = psutil.virtual_memory()
        ram_config = config["memory"]
        msg_config = config["logmsg"]
        soft_max_ram = float(ram_config["max_ram1"])
        hard_max_ram = float(ram_config["max_ram2"])
        ram_message: dict = dict()
        ram_value: dict
        ram_value = {"ram": psutool.percent}
        ram_use_level: str = "INFO"

        if soft_max_ram < psutool.percent < hard_max_ram:
            ram_use_level = "WARNING"
            ram_message = {"ram": msg_config[ram_use_level] + " " + str(psutool.percent)
                                  + "% des Rams werden verbraucht"}
        if psutool.percent > hard_max_ram:
            ram_use_level = "CRITICAL"
            ram_message = {"ram": msg_config[ram_use_level] + " " + str(psutool.percent)
                                  + "% des Rams werden verbraucht"}

        monitordata = MonitoringData(values=ram_value, messages=ram_message,
                                     soft_threshold=soft_max_ram,
                                     hard_threshold=hard_max_ram, log_level=ram_use_level)
        return monitordata
