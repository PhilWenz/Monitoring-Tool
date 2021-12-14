import unittest
from cpu_util import CpuUtil as Cu


class CpuUtilTest(unittest.TestCase):

    def test_cpu_monitoring_data(self):

        config = {
            "cpu": {
                "max_cpu1": 10,
                "max_cpu2": 100},
            "logmsg": {
                "INFO": "Info",
                "WARNING": "Warnung",
                "CRITICAL": "Critical"}
        }

        data = Cu.cpuused(config)
        self.assertIn(container=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], member=data.log_level, msg="Erwarteter loglevel Warning")

if __name__ == '__main__':
    unittest.main()