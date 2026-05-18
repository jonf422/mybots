import numpy as np

#simulation
iterations = 1000
timestep = 1/30

#gravity
gravX = 0
gravY = 0
gravZ = -9.8


#Motors
fl_amplitude = np.pi/4
fl_frequency = 3
fl_phaseShift = 0

bl_amplitude = np.pi/8
bl_frequency = 3
bl_phaseShift = np.pi

motorJointRange = .5

#Neurons
numSensorNeurons = 4
numMotorNeurons = 8

#Evolution
numberOfGenerations = 50
populationSize = 10