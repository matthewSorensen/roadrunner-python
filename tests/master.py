from roadrunnerlib import rrPython
from pkg_resources import resource_filename

import unittest
import inspect

class TestNoFailure(unittest.TestCase):
    """This set of tests calls each method defined for rrPython and
    checks that that it doesn't fail. Replaces the MasterTest.py testbase"""

    def setUp(self):
         rrPython.loadSBMLFromFile(resource_filename('roadrunnerlib','data/feedback.xml'))
       
    def test_information(self):
        """ Tests that all of the methods returning static
        information on this build exist and don't fail """

        self.assertIsNotNone(rrPython.getVersion())
        self.assertIsNotNone(rrPython.getBuildDate())
        self.assertIsNotNone(rrPython.getCopyright())

    def test_load_save_models(self):
        """ Tests that loading and saving SMBL doesn't fail """
        rrPython.loadSBMLFromFile(resource_filename('roadrunnerlib','data/feedback.xml'))
        model = rrPython.getSBML()
        self.assertIsNotNone(model)
        rrPython.loadSBML(model)
    
def test(name,*args):
    """ Add a new test case to TestNoFailure,
    checking that calling a function of rrPython doesn't fail """
    setattr(TestNoFailure,'test_' + name, lambda self:  getattr(rrPython,name)(*args))

# we could do something even eviler! After we add things with all arguments, we just
# bulk create all of the no-arg functions

test('setFloatingSpeciesByIndex',0,1.0)
test('setSteadyStateSelectionList','S1')
test('setSelectionList','time,S1')
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
test('evalModel')
test('getBoundarySpeciesByIndex',0)
test('getBoundarySpeciesByIds')
test('reset')
test('getLastError')
test('getGlobalParameterByIndex',0)
test('getGlobalParameterIds')
test('getGlobalParameterValues')
test('getNumberOfBoundarySpecies')
test('getNumberOfDependentSpecies')
test('getNumberOfCompartments')
test('getNumberOfFloatingSpecies')
test('getNumberOfGlobalParameters')
test('getNumberOfIndependentSpecies')
test('getNumberOfReactions')

"""
#execfile(location + 'computeSteadyStateValues.py')
#execfile(location + 'getAvailableSymbols.py')
#execfile(location + 'getCCodeHeader.py')
#execfile(location + 'getCCodeSource.py')
execfile(location + 'getCapabilities.py')
execfile(location + 'getCompartmentByIndex.py')
execfile(location + 'getCompartmentIds.py')
execfile(location + 'getConcentrationControlCoefficientIds.py')
execfile(location + 'getConservationMatrix.py')
#execfile(location + 'getuCC.py')
#execfile(location + 'getuEE.py')
#execfile(location + 'getCC.py')
#execfile(location + 'getEE.py')
execfile(location + 'getEigenValueIds.py')
execfile(location + 'getElasticityCoefficientIds.py')
execfile(location + 'getFloatingSpeciesByIndex.py')
execfile(location + 'getFloatingSpeciesInitialConcentrations.py')
execfile(location + 'getFloatingSpeciesInitialConditionIds.py')
execfile(location + 'getFloatingSpeciesIds.py')
execfile(location + 'getFloatingSpeciesConcentrations.py')
execfile(location + 'getFluxControlCoefficientIds.py')
#execfile(location + 'getFullJacobian.py')                 Causes crash
execfile(location + 'getLinkMatrix.py')
execfile(location + 'getNrMatrix.py')
execfile(location + 'getL0Matrix.py')
execfile(location + 'getMatrixNumCols.py')
execfile(location + 'getMatrixNumRows.py')
execfile(location + 'getMatrixElement.py')
execfile(location + 'getParamPromotedSBML.py')
execfile(location + 'getRRInstance.py')
execfile(location + 'getRateOfChange.py')
execfile(location + 'getRatesOfChange.py')
execfile(location + 'getRatesOfChangeEx.py')
execfile(location + 'getRatesOfChangeIds.py')
execfile(location + 'getReactionIds.py')
execfile(location + 'getReactionRate.py')
execfile(location + 'getReactionRates.py')
execfile(location + 'getReactionRatesEx.py')
#execfile(location + 'getReducedJacobian.py')
execfile(location + 'getResultColumnLabel.py')
execfile(location + 'getResultElement.py')
execfile(location + 'getResultNumCols.py')
execfile(location + 'getResultNumRows.py')
#execfile(location + 'getScaledElasticityMatrix.py')
#execfile(location + 'getScaledFloatingSpeciesElasticity.py')
execfile(location + 'getSelectionList.py')
execfile(location + 'getSteadyStateSelectionList.py')
execfile(location + 'getStoichiometryMatrix.py')
#execfile(location + 'getStringListElement.py')
#execfile(location + 'getStringListLength.py')
execfile(location + 'getTempFolder.py')
execfile(location + 'getValue.py')
#execfile(location + 'getVectorElement.py')
#execfile(location + 'getVectorLength.py')
#execfile(location + 'hasError.py')
#execfile(location + 'oneStep.py')
execfile(location + 'printList.py')
execfile(location + 'printMatrix.py')
#execfile(location + 'printResult.py')
#execfile(location + 'printVector.py')
#execfile(location + 'setVectorElement.py')
#execfile(location + 'simulate.py')
#execfile(location + 'simulateEx.py')
#execfile(location + 'steadyState.py')

"""

if __name__ == '__main__':
    unittest.main()
