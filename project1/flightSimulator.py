#Simple flight simulator
import numpy
import random
import math
class FlightSimulator:

    def __init__(self, deltaTime):
        self.deltatime = deltaTime#s
        self.heightMax=10.e3# max altitude

        self.maxVelocity = 900.*1000./3600.#max velocity


        self.distance = random.uniform(100e3, 10e6)#in meters
        self.time = 0.
        self.distanceGone = 0.
        self.velocity =0.
        self.altitude =0.
        self.distanceLandStart=self.distance/10.#distance for launch/land
        self.angle = math.atan2(self.heightMax,self.distanceLandStart)
        self.acceleration = pow(self.maxVelocity,2)/(2.*self.distanceLandStart)
        self.flightNumber=numpy.random.randint(10e3,100e3,1)

    def run(self):#set flight number

        return self.flightNumber[0]

    def flight(self):#simulate launch, cruise and landing
        if self.distanceGone < self.distanceLandStart:
            self.startLaunch(True)
            return True
        elif self.distanceGone < (self.distance-self.distanceLandStart):
            self.cruise()
            return True
        elif self.velocity>0:
            self.startLaunch(False)
            return True
        print self.distance
        return False

    def flightParameters(self):#get flight parameters
        return {'velocity':self.velocity, 'altitude':self.altitude, 'time':self.time, 'distanceGone':self.distanceGone,'distance':self.distance}

    def cruise(self):#cruise
        self.time=self.time+self.deltatime
        self.distanceGone=self.distanceGone+self.velocity*self.deltatime


    def startLaunch(self, land):#simulate launch/land
        accdecc = ((lambda:-1, lambda:1)[land]())
        self.velocity=self.velocity+accdecc*self.acceleration*self.deltatime
        self.distanceGone=self.distanceGone+self.velocity*self.deltatime*math.cos(self.angle)
        self.altitude=self.altitude+accdecc*self.velocity*self.deltatime*math.sin(self.angle)
        self.time=self.time+self.deltatime
