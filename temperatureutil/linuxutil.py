from temperatureutil import Util
import os
if os.name == "posix":
    import psutil


class LinuxUtil(Util):

    @staticmethod
    def get_cpu_temp():
        cpu_temp = None
        try:
            sensors = psutil.sensors_temperatures(fahrenheit=False)
            current = 0
            for sensor in sensors["coretemp"]:
                measured = sensor.current
                print(f"{sensor.label}: {sensor.current}")

                if measured > current:
                    current = measured

                cpu_temp = current

        except Exception as e:
            print(e)

        return cpu_temp
