import pyrosim.pyrosim as ps

ps.Start_SDF("box.sdf")
ps.Send_Cube(name="Box", pos=[0,0,.5], size=[1,1,1])
ps.End()