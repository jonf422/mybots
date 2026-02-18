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
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)


for i in range(1000): #simulate for 5000 iterations
    pb.stepSimulation()

    backLegSensorValues[i] = ps.Get_Touch_Sensor_Value_For_Link("BackLeg") #get touch sensor data for front and back leg
    frontLegSensorValues[i] = ps.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    ps.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = pb.POSITION_CONTROL, targetPosition = -np.pi/4, maxForce = 500)
    
    time.sleep(1/60)
    #print(i) #print iteration

pb.disconnect()
np.save("data/backLegSensorValues.npy", backLegSensorValues, True)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues, True)
