import unittest
from temperatureutil import TemperatureUtil as Tu


class TempUtilTest(unittest.TestCase):

    def test_temperature_monitoring_data(self):

        config = {
            "temperature_cpu": {
                "max_temp_cpu1": 0,
                "max_temp_cpu2": 9999},
            "logmsg": {
                "WARNING": "Warnung"}
        }

        data = Tu.cputemperature(config)
        self.assertIn(container=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], member=data.log_level, msg="Erwarteter loglevel Warning")


if __name__ == '__main__':
    unittest.main()