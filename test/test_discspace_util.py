import unittest
from discspace_util import DiscSpaceUtil as d_util


class discspaceUtilTest(unittest.TestCase):

    def test_discspace_monitoring_data(self):

        config1 = {
            "harddrive": {
                "max_discspace1": 0,
                "max_discspace2": 101},
            "logmsg": {
                "WARNING": "Warnung"}
        }


        data = d_util.discspace(config1)
        self.assertEqual("WARNING", data.log_level, "Erwarteter loglevel Warning")



if __name__ == '__main__':
    unittest.main()