from roadrunnerlib import rrPython
from pkg_resources import resource_filename
import tempfile
import unittest

class TestNoFailure(unittest.TestCase):
    """This set of tests calls each method defined for rrPython and
    checks that that it doesn't fail. Replaces the MasterTest.py testbase"""

    def setUp(self):
        None

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
        
# The remaining functiobs from MasterTest.py to import:
    
"""
#execfile(location + 'computeSteadyStateValues.py')
execfile(location + 'evalModel.py')
#execfile(location + 'getAvailableSymbols.py')
execfile(location + 'getBoundarySpeciesByIndex.py')
execfile(location + 'getBoundarySpeciesIds.py')
#execfile(location + 'getCCode.py')
#execfile(location + 'getCCodeHeader.py')
#execfile(location + 'getCCodeSource.py')
execfile(location + 'getCapabilities.py')
execfile(location + 'getCompartmentByIndex.py')
execfile(location + 'getCompartmentIds.py')
execfile(location + 'getConcentrationControlCoefficientIds.py')
execfile(location + 'getConservationMatrix.py')
execfile(location + 'getCopyright.py')
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
execfile(location + 'getGlobalParameterByIndex.py')
execfile(location + 'getGlobalParameterIds.py')
execfile(location + 'getGlobalParameterValues.py')
execfile(location + 'getLastError.py')
execfile(location + 'getLinkMatrix.py')
execfile(location + 'getNrMatrix.py')
execfile(location + 'getL0Matrix.py')
execfile(location + 'getMatrixNumCols.py')
execfile(location + 'getMatrixNumRows.py')
execfile(location + 'getMatrixElement.py')
execfile(location + 'getNumberOfBoundarySpecies.py')
execfile(location + 'getNumberOfCompartments.py')
execfile(location + 'getNumberOfDependentSpecies.py')
execfile(location + 'getNumberOfFloatingSpecies.py')
execfile(location + 'getNumberOfGlobalParameters.py')
execfile(location + 'getNumberOfIndependentSpecies.py')
execfile(location + 'getNumberOfReactions.py')
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
execfile(location + 'reset.py')
execfile(location + 'setBoundarySpeciesByIndex.py')
execfile(location + 'setCapabilities.py')
execfile(location + 'setCompartmentByIndex.py')
execfile(location + 'setComputeAndAssignConservationLaws.py')
execfile(location + 'setFloatingSpeciesByIndex.py')
execfile(location + 'setGlobalParameterByIndex.py')
execfile(location + 'setNumPoints.py')
execfile(location + 'setSelectionList.py')
execfile(location + 'setSteadyStateSelectionList.py')
execfile(location + 'setTempFolder.py')
execfile(location + 'setTimeEnd.py')
execfile(location + 'setTimeStart.py')
execfile(location + 'setValue.py')
#execfile(location + 'setVectorElement.py')
#execfile(location + 'simulate.py')
#execfile(location + 'simulateEx.py')
#execfile(location + 'steadyState.py')

"""


if __name__ == '__main__':
    unittest.main()
