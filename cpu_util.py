import psutil
from monitoring_data import MonitoringData


class CpuUtil:

    @staticmethod
    def cpuused(config):
        cpu_config = config["cpu"]
        msg_config = config["logmsg"]
        soft_max_cpu = float(cpu_config["max_cpu1"])
        hard_max_cpu = float(cpu_config["max_cpu2"])
        cpu_message:dict
        cpu_value:dict
        cpu_value = {"CPU":psutil.cpu_percent(1)}
        cpu_level: str = "INFO"


        try:
            cpu_usage = psutil.cpu_percent(1)
        except Exception as e:
            print(e)

        print(cpu_usage,"%","of CPU wird benutzt")

        if soft_max_cpu < cpu_usage < hard_max_cpu:
            print("Warnung der Cpu!")
            cpu_level = "WARNING"
        if cpu_usage > hard_max_cpu:
            print("Achtung kritische Auslastung der Cpu!")
            cpu_level = "CRITICAL"
        if cpu_usage is not None:
            cpu_message = {"CPU":msg_config[cpu_level] + " " + str(cpu_usage) + "% der Cpu wird verwendet"}
            

        monitordata = MonitoringData(values=cpu_value,messages=cpu_message,soft_threshold=soft_max_cpu,hard_threshold=hard_max_cpu)
        return monitordata

