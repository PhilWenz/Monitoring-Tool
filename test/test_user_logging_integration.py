import unittest
from usermonitoring import UserMonitoring
from alarm import AlarmModule
import io
import sys
from monitoring_data import MonitoringData


class TestUserLogIntegration(unittest.TestCase):

    def test_user_monitoring_alarm_integration(self):
        test_output = io.StringIO()
        sys.stdout = test_output
        am = AlarmModule("", "DEBUG")
        am.log(UserMonitoring.get_logged_in_users(), "INFO")

        self.assertRegex(expected_regex="(INFO:root:name=.*, terminal=.*, host=.*, started=[0-9,\\.]*, pid=.{4,5})|$",
                         text=test_output.getvalue())
        sys.stdout = sys.__stdout__

    def test_empty_user_monitoring_alarm_integration(self):
        test_output = io.StringIO()
        sys.stdout = test_output
        am = AlarmModule("", "DEBUG")

        data = MonitoringData(messages={}, values={})
        am.log(data, "INFO")

        self.assertRegex(expected_regex="(INFO:root:name=.*, terminal=.*, host=.*, started=[0-9,\\.]*, pid=.{4,5})|$",
                         text=test_output.getvalue())
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
