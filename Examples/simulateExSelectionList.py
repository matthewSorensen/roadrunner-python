from roadrunnerlib import rrPython
from pkg_resources import resource_filename

model = resource_filename('roadrunnerlib','data/simple.xml')

rrPython.loadSBMLFromFile(model)
rrPython.setSteadyStateSelectionList('time S1 S2')
results = rrPython.simulateEx(0.0,2.0,20)

print results
