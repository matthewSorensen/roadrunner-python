from roadrunnerlib import rrPython
from pkg_resources import resource_filename

model = resource_filename('roadrunnerlib','data/feedback.xml')
rrPython.loadSBMLFromFile(model)
results = rrPython.simulateEx(0.0,2.0,20)

print results
