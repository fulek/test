#Here is the main program which manages all the rest of the filght parameters recorder
import inputReaderValidator
import runDaemon



'''inpt = inputReaderValidator.InputReaderValidator()
while inpt.newPlane():
    delay = inpt.delayTime()
    plane = recordDaemon.RecordDaemon(delay)
    plane.newPlane()'''

aaa = runDaemon.RunDaemon(1)
aaa.run()
