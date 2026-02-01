import pyrosim.pyrosim as ps

def Create_World():

    ps.Start_SDF("world.sdf")

    ps.Send_Cube(name="Box", pos=[-4,4,.5], size=[1,1,1])
    ps.End()

def Create_Robot():
    ps.Start_URDF("body.urdf")

    ps.Send_Cube(name="Link0", pos=[0,0,0.5], size=[1,1,1])
    ps.Send_Cube(name="Link1", pos=[0,0,0.5], size=[1,1,1])
    ps.Send_Cube(name="Link2", pos=[0,0,0.5], size=[1,1,1])

    ps.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0,0,1])
    ps.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute",position=[0,0,1])

    ps.End()

Create_World()
Create_Robot()