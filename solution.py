import numpy as np
import os
import pyrosim.pyrosim as ps
import random
import time
import constants as c

class SOLUTION:

    def __init__(self, ID):
        self.myID = ID
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = 2*self.weights-1

        self.legLengths = 3*np.random.rand(1,2)+.5


    def Start_Simulation(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"start /B python simulate.py {mode} {self.myID}")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(0.01)

        with open(f"fitness{self.myID}.txt", "r") as file:
            self.fitness = float(file.read())
            #print(self.fitness)

        os.system(f"del fitness{self.myID}.txt")

    def Create_World(self):

        ps.Start_SDF("world.sdf")

        ps.Send_Cube(name="Box", pos=[-4,4,.5], size=[1,1,1])
        ps.End()

    def Create_Body(self):
        ps.Start_URDF("body.urdf")

        #Torso
        ps.Send_Cube(name="Torso", pos=[0,0,1], size=[1,1,1])

        #Front Leg
        ps.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",position=[0,.5,1], jointAxis="1 0 0")
        ps.Send_Cube(name="FrontLeg", pos=[0,0.5,0], size=[.2,1,.2])
        ps.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg", type="revolute", position=[0,1,0], jointAxis="1 0 0")
        ps.Send_Cube(name="LowerFrontLeg", pos=[0,0,-0.5], size=[.2,.2,1])

        #Back Leg
        ps.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0,-.5,1], jointAxis="1 0 0")
        ps.Send_Cube(name="BackLeg", pos=[0,-.5,0], size=[.2,1,.2])
        ps.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg", type="revolute", position=[0,-1,0], jointAxis="1 0 0")
        ps.Send_Cube(name="LowerBackLeg", pos=[0,0,-0.5], size=[.2,.2,1])
        
        #Left Leg
        ps.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-.5,0,1], jointAxis="0 1 0")
        ps.Send_Cube(name="LeftLeg", pos=[-.5,0,0], size=[1.0,.2,.2])
        ps.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg", type="revolute", position=[-1,0,0], jointAxis="0 1 0")
        ps.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.5], size=[.2,.2,1])

        #Right Leg
        ps.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[.5,0,1], jointAxis="0 1 0")
        ps.Send_Cube(name="RightLeg", pos=[.5,0,0], size=[1.0,.2,.2])
        ps.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg", child="LowerRightLeg", type="revolute", position=[1,0,0], jointAxis="0 1 0")
        ps.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.5], size=[.2,.2,1])
        
        ps.End()

    def Create_Brain(self):
        ps.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        #ps.Send_Sensor_Neuron(name=0, linkName="Torso")
        #ps.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        #ps.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        #ps.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        #ps.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        ps.Send_Sensor_Neuron(name=0, linkName="LowerFrontLeg")
        ps.Send_Sensor_Neuron(name=1, linkName="LowerBackLeg")
        ps.Send_Sensor_Neuron(name=2, linkName="LowerLeftLeg")
        ps.Send_Sensor_Neuron(name=3, linkName="LowerRightLeg")

        ps.Send_Motor_Neuron(name=4, jointName="Torso_BackLeg")
        ps.Send_Motor_Neuron(name=5, jointName="Torso_FrontLeg")
        ps.Send_Motor_Neuron(name=6, jointName="Torso_LeftLeg")
        ps.Send_Motor_Neuron(name=7, jointName="Torso_RightLeg")
        ps.Send_Motor_Neuron(name=8, jointName="FrontLeg_LowerFrontLeg")
        ps.Send_Motor_Neuron(name=9, jointName="BackLeg_LowerBackLeg")
        ps.Send_Motor_Neuron(name=10, jointName="LeftLeg_LowerLeftLeg")
        ps.Send_Motor_Neuron(name=11, jointName="RightLeg_LowerRightLeg")

    
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                ps.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])

        ps.End()

    def Mutate(self):
        randRow = random.randint(0,c.numSensorNeurons-1)
        randCol = random.randint(0,c.numMotorNeurons-1)
        self.weights[randRow, randCol] = 2*random.random()-1

        randlength = random.randint(0,1)
        self.legLengths[0, randlength] = 3*random.random()+.5
        print(f'Upper legs: {self.legLengths[0,0]} Lower legs: {self.legLengths[0,1]}')

    def Set_ID(self, ID):
        self.myID = ID