from roadrunnerlib import rrPython
from pkg_resources import resource_filename

import unittest

class TestBasicFunctionality(unittest.TestCase):
    def setUp(self):
        None

    def test_awesomeness(self):
        True

    def test_load_and_simulate(self):
        model = resource_filename('roadrunnerlib','data/feedback.xml')
        rrPython.loadSBMLFromFile(model)
        rrPython.simulate()

if __name__ == '__main__':
    unittest.main()
