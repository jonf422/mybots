import numpy as np
import constants as c
import pyrosim.pyrosim as ps

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.Prepare_to_Sense()
        
    def Prepare_to_Sense(self):
        self.values = np.zeros(c.iterations)

    def Get_Value(self, t):
        self.values[t] = ps.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
    def Save_Values(self):
        np.save("data/"+str(self.linkName), self.values, True)
        