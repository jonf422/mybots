import pybullet as pb

class WORLD:
    def __init__(self):
        self.planeId = pb.loadURDF("plane.urdf") #load floor plane
        pb.loadSDF("world.sdf") #load world