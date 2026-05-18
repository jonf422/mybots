from world import WORLD
from robot import ROBOT
import constants as c

import pybullet as pb
import pybullet_data
import pyrosim.pyrosim as ps

import numpy as np
import time


class SIMULATION:
    def __init__(self, mode, ID):
        self.mode = mode
        self.ID = ID
        if self.mode == "DIRECT":
            self.physicsClient = pb.connect(pb.DIRECT) #set up pybullet
        else:
            self.physicsClient = pb.connect(pb.GUI)
        pb.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD(self.ID)
        self.robot = ROBOT(self.ID)

        pb.setGravity(c.gravX,c.gravY,c.gravZ) #set gravity

    def __del__(self):
        '''
        for s in self.robot.sensors:
            self.robot.sensors[s].Save_Values()
        for m in self.robot.motors:
            self.robot.motors[m].Save_Values()
        '''
        pb.disconnect()


    def Run(self):
        for i in range(c.iterations): #simulate for __ iterations
            pb.stepSimulation()

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            if self.mode == "GUI": time.sleep(c.timestep)
            #print(i) #print iteration
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()