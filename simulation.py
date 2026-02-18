import pybullet as pb
import pybullet_data
import pyrosim.pyrosim as ps
import numpy as np
import time
import random

#VARIABLES
fl_amplitude = np.pi/4
fl_frequency = .5
fl_phaseShift = 0

bl_amplitude = np.pi/8
bl_frequency = 10
bl_phaseShift = 0


physicsClient = pb.connect(pb.GUI) #set up pybullet
pb.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = pb.loadURDF("plane.urdf") #load floor plane

robotId = pb.loadURDF("body.urdf") #load robot plane

pb.loadSDF("world.sdf") #load world
pb.setGravity(0,0,-9.8) #set gravity

ps.Prepare_To_Simulate(robotId) #prepare pyrosim for sensor simulation
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

x = np.linspace(0, 2*np.pi, 1000)
fl_targetAngles = fl_amplitude * np.sin(fl_frequency*x + fl_phaseShift)
bl_targetAngles = bl_amplitude * np.sin(bl_frequency*x + bl_phaseShift)

#np.save("data/fl_targetAngles", fl_targetAngles, True)
#np.save("data/bl_targetAngles", bl_targetAngles, True)
#exit()

for i in range(1000): #simulate for 5000 iterations
    pb.stepSimulation()

    backLegSensorValues[i] = ps.Get_Touch_Sensor_Value_For_Link("BackLeg") #get touch sensor data for front and back leg
    frontLegSensorValues[i] = ps.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    ps.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = pb.POSITION_CONTROL, targetPosition = bl_targetAngles[i], maxForce = 500)
    ps.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = pb.POSITION_CONTROL, targetPosition = fl_targetAngles[i], maxForce = 500)
    
    time.sleep(1/60)
    #print(i) #print iteration

pb.disconnect()
np.save("data/backLegSensorValues.npy", backLegSensorValues, True)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues, True)
