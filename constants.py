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

#Neurons
numSensorNeurons = 3
numMotorNeurons = 2

#Evolution
numberOfGenerations = 1
populationSize = 1