from roadrunnerlib import rrPython
from pkg_resources import resource_filename

import unittest

class TestBasicFunctionality(unittest.TestCase):
    def setUp(self):
        None

    def test_load_and_simulate(self):
        rrPython.loadSBMLFromFile(resource_filename('roadrunnerlib','feedback.xml'))
        rrPython.simulate()

if __name__ == '__main__':
    unittest.main()
