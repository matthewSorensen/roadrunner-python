from roadrunnerlib import rrPython
from pkg_resources import resource_filename

import os

model = resource_filename('roadrunnerlib','feedback.xml')

sbml = rrPython.loadSBMLFromFile(model)
rrPython.setTimeStart(0.0)
rrPython.setTimeEnd(3.0)
rrPython.setNumPoints(20)
rrPython.setSteadyStateSelectionList("time S1 S2 S3 S4")
results = rrPython.simulate()

print results
