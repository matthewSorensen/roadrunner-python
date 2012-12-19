from roadrunnerlib import rrPython
from pkg_resources import resource_filename

import unittest
import inspect
import types
import sys

def covers(functions, d = set([])):
    d |= set(functions)
    return d


class TestNoFailure(unittest.TestCase):
    """This set of tests calls each method defined for rrPython and
    checks that that it doesn't fail. Replaces the MasterTest.py testbase"""

    def setUp(self):
         rrPython.loadSBMLFromFile(resource_filename('roadrunnerlib','data/feedback.xml'))
       
    def test_information(self):
        """ Tests that all of the methods returning static
        information on this build exist and don't fail """

        covers(['getVersion','getBuildDate','getCopyright'])

        self.assertIsNotNone(rrPython.getVersion())
        self.assertIsNotNone(rrPython.getBuildDate())
        self.assertIsNotNone(rrPython.getCopyright())

    def test_load_save_models(self):
        """ Tests that loading and saving SMBL doesn't fail """
        covers(['loadSBMLFromFile','getSBML','loadSBML'])

        rrPython.loadSBMLFromFile(resource_filename('roadrunnerlib','data/feedback.xml'))
        model = rrPython.getSBML()
        self.assertIsNotNone(model)
        rrPython.loadSBML(model)
   
# Adding somewhat meaningful tests for everything else is future work.
# In the meantime, all other functions are simply executed - not throwing
# an exception or segfaulting is taken as success.

# In order to eliminate much boilerplate, this is automated.
 
def test(name,*args):
    """ Add a new test case to TestNoFailure,
    checking that calling a function of rrPython doesn't fail """
    def make_test(name,args):
        covers([name])
        getattr(rrPython,name)(*args)
    setattr(TestNoFailure,'test_' + name, lambda self: make_test(name,args))

def defined_in_module(module):
    """ Returns a dict mapping function name to body for all
    functions defined in the supplied module """
    ret = {}
    for function in dir(module):
        body = module.__dict__.get(function)
        parent = inspect.getmodule(body)
        if isinstance(body, types.FunctionType) and parent is module:
            ret[function] = body
    return ret

def derive_nullary_tests(functions,to_ignore):
    """ Generates a test for all functions of zero arguments """
    for name, body in functions.iteritems():
        spec = inspect.getargspec(body)
        if not spec.args and not spec.varargs and name not in to_ignore:
            test(name)

functions = defined_in_module(rrPython)

ignore = set(['getCurrentSBML', 'getUnScaledElasticityMatrix','enableLogging'])

derive_nullary_tests(functions,ignore)


test('setFloatingSpeciesByIndex',0,1.0)
test('setSteadyStateSelectionList','S1')
test('setCompartmentByIndex',0,1.0)
test('setValue','S1',1.0)
test('setNumPoints',10)
test('setTimeStart',0.0)
test('setTimeEnd',5.0)
test('setCapabilities','aaa')
test('setTempFolder','.')
test('setBoundarySpeciesByIndex',0,1.0)
test('setGlobalSpeciesByIndex',0,1.0)
test('setFloatingSpeciesByIndex',0,1.0)
test('setComputeAndAssignConservationLaws','1')
test('getBoundarySpeciesByIndex',0)
test('getGlobalParameterByIndex',0)


if __name__ == '__main__':
    # Most of the time we don't want the list of functions that weren't covered or
    # ignored. If that is desired, add the --untested flag.
    display_untested = '--untested' in sys.argv

    if display_untested: sys.argv.remove('--untested')

    try: unittest.main()
    finally:
        unseen = set(functions.keys()) - covers([]) - ignore
        f = len(functions)
        print 'Covered ',  round(100 * (f - len(unseen)) / f), '% of module functions'
        if '--untested' in sys.argv:
            for function in unseen:
                print function, ' is untested'
