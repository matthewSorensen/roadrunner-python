from roadrunnerlib import rrPython
from pkg_resources import resource_filename

print 'RoadRunner Python'
print rrPython.getCopyright()
print 'Build on ' + rrPython.getBuildDate()

startTime = 0
endTime = 5
numPoints = 50
selList="time,S1,S2"


model = resource_filename('roadrunnerlib','data/test_1.xml')
result = rrPython.loadSBMLFromFile(model)

rrPython.setTimeStart(startTime)
rrPython.setTimeEnd(endTime)
rrPython.setNumPoints(numPoints)
rrPython.setTimeCourseSelectionList(selList)
k = rrPython.simulate()

print k

