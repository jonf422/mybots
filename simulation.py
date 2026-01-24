import pybullet as pb
import time

physicsClient = pb.connect(pb.GUI)

pb.loadSDF("box.sdf")
for i in range(1000):
    pb.stepSimulation()
    time.sleep(1/60)
    print(i)
pb.disconnect()