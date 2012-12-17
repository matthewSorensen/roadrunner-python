from roadrunnerlib import rrPython
from pkg_resources import resource_filename

model = resource_filename('roadrunnerlib','data/feedback.xml')
rrPython.loadSBMLFromFile(model)
matrix = rrPython.getStoichiometryMatrix()

print matrix
