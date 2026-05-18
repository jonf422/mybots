import pybullet as pb
import os

class WORLD:
    def __init__(self, ID):
        self.planeId = pb.loadURDF("plane.urdf") #load floor plane
        pb.loadSDF(f"world{ID}.sdf") #load world
        os.system(f"del world{ID}.sdf")