import pyrosim.pyrosim as ps
import pybullet as pb
import numpy as np
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        
        
    def Set_Value(self, robot, desiredAngle):
        ps.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = pb.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = 500)