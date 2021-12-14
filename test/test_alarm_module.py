import unittest
import io
import sys

from alarm import AlarmModule
from monitoring_data import MonitoringData


class TestAlarmModule(unittest.TestCase):
    def test_alarm_single_line(self):
        # Testen des neuen Alarmmoduls
        test_output = io.StringIO()
        sys.stdout = test_output

        am = AlarmModule(log_file_url="", log_level="DEBUG")
        am.log(MonitoringData(log_level="DEBUG", values={}, messages={"V1": "Test123"}, soft_threshold=1, hard_threshold=2))
        self.assertEqual("DEBUG:root:Test123\n", test_output.getvalue(), "Konsolenoutput")
        sys.stdout = sys.__stdout__

    def test_alarm_multi_line(self):
        test_output = io.StringIO()
        sys.stdout = test_output
        am = AlarmModule(log_file_url="", log_level="DEBUG")
        am.log(MonitoringData(log_level="DEBUG", values={"Value1": 5, "Value2": 6}, messages={}))
        self.assertEqual("DEBUG:root:Value1: 5\nDEBUG:root:Value2: 6\n", test_output.getvalue(), "Multiline Konsolenoutput")
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
