from sensor import SENSOR
from motor import MOTOR
import pybullet as pb
import pyrosim.pyrosim as ps
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
import numpy as np
import os

class ROBOT:
    def __init__(self, ID):
        self.robot = pb.loadURDF(f"body{ID}.urdf") #load robot
        self.nn = NEURAL_NETWORK(f"brain{ID}.nndf")
        self.ID = ID

        ps.Prepare_To_Simulate(self.robot) #prepare pyrosim for sensor simulation
        self.Prepare_to_Sense()
        self.Prepare_to_Act()
        os.system(f"del body{self.ID}.urdf")
        os.system(f"del brain{self.ID}.nndf")

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
            #print(jointName)
        
    def Act(self, t):
        for n in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(n):
                jointName = self.nn.Get_Motor_Neurons_Joint(n).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(n) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robot, desiredAngle)
                jointName = jointName.decode("utf-8")
                #print(n)
                #print(jointName)
                #print(desiredAngle)
                #print()

        #for motor in self.motors.values():
         #   motor.Set_Value(self.robot, desiredAngle)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()
    
    def Get_Fitness(self):
        basePositionAndOrientation = pb.getBasePositionAndOrientation(self.robot)
        #print(stateOfLinkZero)
        basePosition = basePositionAndOrientation[0]
        #print(positionOfLinkZero)
        xCoordinateOfLinkZero = basePosition[0]
        #print(xCoordinateOfLinkZero)
        with open(f"tmp{self.ID}.txt", "w") as file:
            file.write(str(xCoordinateOfLinkZero))
        os.system(f"rename tmp{self.ID}.txt fitness{self.ID}.txt")