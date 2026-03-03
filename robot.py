from sensor import SENSOR
from motor import MOTOR
import pybullet as pb
import pyrosim.pyrosim as ps
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
import numpy as np

class ROBOT:
    def __init__(self):
        self.robot = pb.loadURDF("body.urdf") #load robot
        self.nn = NEURAL_NETWORK("brain.nndf")

        ps.Prepare_To_Simulate(self.robot) #prepare pyrosim for sensor simulation
        self.Prepare_to_Sense()
        self.Prepare_to_Act()

    #Sensors
    def Prepare_to_Sense(self):
        self.sensors = {}
        for linkName in ps.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, t):
        for i in self.sensors.values():
            i.Get_Value(t)

    #Motors
    def Prepare_to_Act(self):
        self.motors = {}
        for jointName in ps.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            print(jointName)
        
    def Act(self, t):
        for n in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(n):
                jointName = self.nn.Get_Motor_Neurons_Joint(n)
                desiredAngle = self.nn.Get_Value_Of(n)
                print(n)
                print(jointName)
                print(desiredAngle)
        
    def Think(self):
        self.nn.Update()
        self.nn.Print()