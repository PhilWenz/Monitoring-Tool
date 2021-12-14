import unittest
from alarm import LogAlarm


class LogLevelTest(unittest.TestCase):
    def test_parse_level(self):

        logger = LogAlarm("", "DEBUG")
        self.assertEqual(10, logger.parse_level("DEBUG"), "DEBUG Loglevel")
        self.assertEqual(20, logger.parse_level("INFO"), "INFO Loglevel")
        self.assertEqual(30, logger.parse_level("WARNING"), "WARNING Loglevel")
        self.assertEqual(40, logger.parse_level("ERROR"), "ERROR Loglevel")
        self.assertEqual(50, logger.parse_level("CRITICAL"), "CRITICAL Loglevel")

    def test_get_level(self):
        logger = LogAlarm("", "ERROR")
        self.assertEqual(LogAlarm.ERROR, logger.level)

#test
if __name__ == "__main__":
    unittest.main()
