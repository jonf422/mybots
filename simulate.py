import pybullet as pb
import pybullet_data
import pyrosim.pyrosim as ps
import numpy as np
import time
import random
import constants as c
from simulation import SIMULATION
from world import WORLD
from robot import ROBOT

simulation = SIMULATION()
simulation.Run()

'''

x = np.linspace(0, 2*np.pi, c.iterations)
fl_targetAngles = c.fl_amplitude * np.sin(c.fl_frequency*x + c.fl_phaseShift)
bl_targetAngles = c.bl_amplitude * np.sin(c.bl_frequency*x + c.bl_phaseShift)

#np.save("data/fl_targetAngles", fl_targetAngles, True)
#np.save("data/bl_targetAngles", bl_targetAngles, True)
#exit()



pb.disconnect()
np.save("data/backLegSensorValues.npy", backLegSensorValues, True)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues, True)
'''