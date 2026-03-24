import numpy as np
import os
import pyrosim.pyrosim as ps
import random

class SOLUTION:

    def __init__(self):
        self.weights = np.random.rand(3,2)
        self.weights = 2*self.weights-1

    def Evaluate(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python simulate.py DIRECT")
        with open("fitness.txt", "r") as file:
            self.fitness = float(file.read())

    def Create_World(self):

        ps.Start_SDF("world.sdf")

        ps.Send_Cube(name="Box", pos=[-4,4,.5], size=[1,1,1])
        ps.End()

    def Create_Body(self):
        ps.Start_URDF("body.urdf")

        ps.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1])

        
        ps.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1,0,1])
        ps.Send_Cube(name="BackLeg", pos=[-0.5,0,-.5], size=[1,1,1])
        
        ps.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",position=[2,0,1])
        ps.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
        
        ps.End()

    def Create_Brain(self):
        ps.Start_NeuralNetwork("brain.nndf")

        ps.Send_Sensor_Neuron(name=0, linkName="Torso")
        ps.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        ps.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        ps.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        ps.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    
        for currentRow in range(3):
            for currentColumn in range(2):
                ps.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])

        ps.End()

    def Mutate(self):
        randRow = random.randint(0,2)
        randCol = random.randint(0,1)

        self.weights[randRow, randCol] = 2*random.random()-1