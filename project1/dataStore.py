#Store data. Save to file and tar it if #entries == 10k. Also here read data and draw plots.
import tarfile
import os
class DataStore:
    def __init__(self,flightNumber):
        self.flightNumber=flightNumber

    def openNewFile(self, number):#open new file
        self.target = open(self.flightNumber+"_"+str(int(number) )+".txt", 'w')

    def writeToFile(self,parameters):#write to file
        self.target.write(str(parameters))
        self.target.write("\n")

    def closeFile(self):#close file
        self.target.close()

    def targzFile(self):#tar gz file
        tar = tarfile.open(self.flightNumber+".tar.gz", "w:gz")
        for name in self.findAlltextFile():
            tar.add(name)
        tar.close()
        self.removeTxt()

    def findAlltextFile(self):#find all text files
        files = []
        for file in os.listdir("./"):
            if file.endswith(".txt") and file.startswith(self.flightNumber+"_"):
                files.append(file)
        return files

    def removeTxt(self):# remove all text files
        for file in self.findAlltextFile():
            os.remove(file)
