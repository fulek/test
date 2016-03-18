#Here is the thread class which creates new plane

import threading
import time
import flightSimulator
import dataStore


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

    def printFlightParameters(self):
        return self.plane.flightParameters()

    def closeOpen(self):
        self.file.closeFile()
        self.file.openNewFile(self.counter/self.maxEvents)

