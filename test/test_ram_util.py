import unittest
from ram_util import RamUtil as r_util


class ramUtilTest(unittest.TestCase):

    def test_ram_monitoring_data(self):

        config1 = {
            "memory": {
                "max_ram1": 0,
                "max_ram2": 101},
            "logmsg": {
                "WARNING": "Warnung"}
        }
        config2 = {
            "memory": {
                "max_ram1": 0,
                "max_ram2": 0},
            "logmsg": {
                "WARNING": "Warnung",
                "CRITICAL": "Kritische Warnung"}
        }

        data = r_util.ramused(config1)
        self.assertEqual("WARNING", data.log_level, "Erwarteter loglevel Warning")
        data = r_util.ramused(config2)
        self.assertEqual("CRITICAL", data.log_level, "Erwarteter loglevel CRITICAL")


if __name__ == '__main__':
    unittest.main()