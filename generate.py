import pyrosim.pyrosim as ps

def Create_World():

    ps.Start_SDF("world.sdf")

    ps.Send_Cube(name="Box",pos=[-4,4,.5], size=[1,1,1])
    ps.End()

def Create_Robot():
    ps.Start_URDF("body.urdf")

    ps.Send_Cube(name="Torso",pos=[0,0,.5], size=[1,1,1])

    ps.End()

Create_World()
Create_Robot()