import pyrosim.pyrosim as ps

def Create_World():

    ps.Start_SDF("world.sdf")

    ps.Send_Cube(name="Box", pos=[-4,4,.5], size=[1,1,1])
    ps.End()

def Create_Robot():
    ps.Start_URDF("body.urdf")

    ps.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1])

    
    ps.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1,0,1])
    ps.Send_Cube(name="BackLeg", pos=[-0.5,0,-.5], size=[1,1,1])
    
    ps.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",position=[2,0,1])
    ps.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
    
    ps.End()

Create_World()
Create_Robot()