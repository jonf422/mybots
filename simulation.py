import pybullet as pb
import pybullet_data

import time

physicsClient = pb.connect(pb.GUI)
pb.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = pb.loadURDF("plane.urdf") #load floor plane

robotId = pb.loadURDF("body.urdf") #load robot plane

pb.loadSDF("world.sdf") #load world
pb.setGravity(0,0,-9.8) #set gravity

for i in range(1000): #simulate for 1000 iterations
    pb.stepSimulation()
    time.sleep(1/60)
    print(i)
pb.disconnect()