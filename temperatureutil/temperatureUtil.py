import os
if os.name == "nt":
    from temperatureutil import WindowsUtil as Ut
elif os.name == "posix":
    from temperatureutil import LinuxUtil as Ut
from monitoring_data import MonitoringData


class TemperatureUtil:

    @staticmethod
    def cputemperature(config):
        cputemps_config = config["temperature_cpu"]
        msg_config = config["logmsg"]
        soft_maxtemp_cpu = float(cputemps_config["max_temp_cpu1"])
        hard_maxtemp_cpu = float(cputemps_config["max_temp_cpu2"])  
        cpu_temp_message:dict
        cpu_temp_value:dict
        cpu_temp_value = {"Temp":Ut.get_cpu_temp()}
        cpu_temp_level: str = "INFO"


        try:
            cpu_temp = Ut.get_cpu_temp()
        except Exception as e:
            print(e) 

        print(f"INFO: Die CPU Temperatur beträgt {cpu_temp}°C")

        if cpu_temp is not None:
            if soft_maxtemp_cpu < cpu_temp < hard_maxtemp_cpu:
                print("Warnung wegen hoher Cpu Temperatur")
                print(str(cpu_temp), "°C der CPU")
                cpu_temp_level= "WARNING"
            if cpu_temp > hard_maxtemp_cpu:
                print("Kritische Temperatur!")
                print(str(cpu_temp),"°C der CPU")
                cpu_temp_level = "CRITICAL"
            cpu_temp_message = {"Temp":msg_config[cpu_temp_level] + " " + str(cpu_temp) + "°C beträgt die CPU"}

        if cpu_temp is None:
            cpu_temp_level = "ERROR"
            cpu_temp_message = {"Temp":"Open Hardware Monitor nicht gefunden"}

 
        monitordata = MonitoringData(values=cpu_temp_value,messages=cpu_temp_message,soft_threshold=soft_maxtemp_cpu,hard_threshold=hard_maxtemp_cpu, log_level=cpu_temp_level)
        return monitordata


        #if gpu_value > maxtempgpu1 and gpu_value < maxtempgpu2:
        #    print("Warnung wegen hoher Gpu Temperatur")
        #    print(str(cpu_value), "°C der CPU")
        #if gpu_value > maxtempgpu2:
        #    print("Kritische Temperatur!")
        #    print(str(cpu_value),"°C der GPU")