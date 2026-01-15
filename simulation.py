import pybullet as pb
import time

physicsClient = pb.connect(pb.GUI)
for i in range(1000):
    pb.stepSimulation()
    time.sleep(1/60)
    print(i)
pb.disconnect()