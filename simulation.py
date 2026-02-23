from world import WORLD
from robot import ROBOT
import constants as c

import pybullet as pb
import pybullet_data
import pyrosim.pyrosim as ps

import numpy as np
import time


class SIMULATION:
    def __init__(self):
        self.physicsClient = pb.connect(pb.GUI) #set up pybullet
        pb.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT()

        pb.setGravity(c.gravX,c.gravY,c.gravZ) #set gravity

    def __del__(self):
        pb.disconnect()


    def Run(self):
        for i in range(c.iterations): #simulate for __ iterations
            pb.stepSimulation()

            self.robot.Sense(i)

            #ps.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = pb.POSITION_CONTROL, targetPosition = bl_targetAngles[i], maxForce = 500)
            #ps.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = pb.POSITION_CONTROL, targetPosition = fl_targetAngles[i], maxForce = 500)

            time.sleep(c.timestep)
            #print(i) #print iteration