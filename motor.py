import pyrosim.pyrosim as ps
import pybullet as pb
import numpy as np
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_to_Act()

    def Prepare_to_Act(self):
        self.amplitude = c.fl_amplitude
        self.frequency = c.fl_frequency
        self.phaseShift = c.fl_phaseShift
        self.motorValues = np.zeros(c.iterations)

        if(self.jointName == b'Torso_FrontLeg'):
            self.frequency = c.fl_frequency / 2

        x = np.linspace(0, 2*np.pi, c.iterations)
        self.motorValues = self.amplitude * np.sin(self.frequency*x + self.phaseShift)
        
    def Set_Value(self, robot, t):
        ps.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = pb.POSITION_CONTROL, targetPosition = self.motorValues[t], maxForce = 500)

    
    def Save_Values(self):
        np.save("data/"+str(self.jointName), self.motorValues, True)