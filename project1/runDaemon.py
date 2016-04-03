#Here is the thread class which simulates plane and reads parameters

from multiprocessing import Process
import time
import flightSimulator
import dataStore

class RunDaemon():
    def __init__(self, deltaTime):
        self.deltaTime = deltaTime
        self.plane = flightSimulator.FlightSimulator(deltaTime)
        self.name = self.plane.run()
        self.file = dataStore.DataStore(self.name)
        self.counter = 0
        self.maxEvents = 10e2

    def planeFlight(self):
        print "plane flight"
        while self.plane.flight():
            self.plane.flight()
            self.counter+=1
            print self.plane.flightParameters()

    def closeOpen(self):
        self.file.closeFile()
        self.file.openNewFile(self.counter/self.maxEvents)

    def checkIfcloseFile(self):
        if(self.counter%self.maxEvents==0):
                self.closeOpen()

    def readerParams(self):
        print "read"
        self.file.writeToFile(self.plane.flightParameters())
        self.checkIfcloseFile()
        print self.plane.flightParameters()

    def runTwoprocesses(self):
        p1 = Process(target = self.planeFlight)
        p1.start()
        '''p1.join()
        p2 = Process(target = self.readerParams)
        p2.start()
        p2.join()'''

    def run(self):
        print "Starting " + str(self.name)
        self.file.openNewFile(self.counter/self.maxEvents)
        self.runTwoprocesses()
       # self.planeFly(self.deltaTime)
        self.file.closeFile()
        self.file.targzFile()
        print "Exiting " + str(self.name)
'''
class RunDaemon (threading.Thread):
    def __init__(self, deltaTime):
        threading.Thread.__init__(self)

        self.deltaTime = deltaTime
        self.plane = flightSimulator.FlightSimulator(deltaTime)
        self.name = self.plane.run()
        self.file = dataStore.DataStore(self.name)
        self.counter = 0
        self.maxEvents = 10e2

    def planeFly(self, delay):

        while self.plane.flight():
            self.file.writeToFile(self.printFlightParameters())
            #print self.printFlightParameters()
            self.counter+=1
            if(self.counter%self.maxEvents==0):
                self.closeOpen()
            time.sleep(delay)


    def run(self):
        print "Starting " + self.name
        self.file.openNewFile(self.counter/self.maxEvents)
        self.planeFly(self.deltaTime)
        self.file.closeFile()
        self.file.targzFile()
        print "Exiting " + self.name





'''