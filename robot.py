from sensor import SENSOR
from motor import MOTOR
import pybullet as pb
import pyrosim.pyrosim as ps

class ROBOT:
    def __init__(self):
        self.motors = {}
        self.robotId = pb.loadURDF("body.urdf") #load robot
        ps.Prepare_To_Simulate(self.robotId) #prepare pyrosim for sensor simulation
        self.Prepare_to_Sense()

    def Prepare_to_Sense(self):
        self.sensors = {}
        for linkName in ps.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, t):
        for i in self.sensors.values():
            i.Get_Value(t)
        