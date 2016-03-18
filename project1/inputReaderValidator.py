class InputReaderValidator:
    def checkNewPlane(self,plane):# validate new plane
        if plane=='Y':
            return 1
        elif plane == 'N':
            return 0
        else:
            return -1

    def newPlane(self):#check whether monitor new plane
        loop = True
        while loop:
            loop= self.checkNewPlane(raw_input("New plane Y/N?"))
            if not loop==-1:
                return loop

    def checkIfFloat(self,x):#check if number is float
        try:
            float(x)
            return float(x) > 0
        except ValueError:
            pass


    def delayTime(self):#get delay time
        delay = False
        while not delay:

            x = raw_input("Give delay in [s]: ")
            delay = self.checkIfFloat(x)
            if delay:
                return float(x)

