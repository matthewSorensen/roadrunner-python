from roadrunnerlib import rrPython


print 'RoadRunner Python'
print rrPython.getCopyright()
print 'Build on ' + rrPython.getBuildDate()

startTime = 0
endTime = 5
numPoints = 50
selList="time,S1,S2"

result = rrPython.loadSBMLFromFile("/usr/local/install/models/test_1.xml")

rrPython.setTimeStart(startTime)
rrPython.setTimeEnd(endTime)
rrPython.setNumPoints(numPoints)
rrPython.setTimeCourseSelectionList(selList)
k = rrPython.simulate()

print k

