import os

from temperatureutil import Util
import os
if os.name == "nt":
    import wmi


class WindowsUtil(Util):

    @staticmethod
    def get_cpu_temp():
        cpu_value = None
        try:
            w = wmi.WMI(namespace="root\OpenHardwareMonitor")
            sensors = w.Sensor()

            for sensor in sensors:
                if sensor.SensorType == u'Temperature' and 'CPU' in sensor.Name:
                    cpu_value = sensor.Value

        except Exception as e:
            print("OpenHardwareMonitor wurde nicht gefunden.")

        return cpu_value
