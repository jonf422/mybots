import pybullet as pb
import pybullet_data
import pyrosim.pyrosim as ps
import numpy as np
import time

physicsClient = pb.connect(pb.GUI) #set up pybullet
pb.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = pb.loadURDF("plane.urdf") #load floor plane

robotId = pb.loadURDF("body.urdf") #load robot plane

pb.loadSDF("world.sdf") #load world
pb.setGravity(0,0,-9.8) #set gravity

ps.Prepare_To_Simulate(robotId) #prepare pyrosim for sensor simulation
backLegSensorValues = np.zeros(10000)


for i in range(5000): #simulate for 5000 iterations
    pb.stepSimulation()

    backLegSensorValues[i] = ps.Get_Touch_Sensor_Value_For_Link("BackLeg")

    time.sleep(1/60)
    #print(i) #print iteration

pb.disconnect()
print(backLegSensorValues)