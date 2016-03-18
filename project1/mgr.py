#Here is the main program which manages all the rest of the filght parameters recorder
import recordDaemon
import inputReaderValidator



inpt = inputReaderValidator.InputReaderValidator()
while inpt.newPlane():
    delay = inpt.delayTime()
    plane = recordDaemon.RecordDaemon(delay)
    plane.newPlane()
