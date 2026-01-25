import pyrosim.pyrosim as ps

length=1
width=2
height=3

ps.Start_SDF("box.sdf")
ps.Send_Cube(name="Box", pos=[0,0,.5], size=[length,width,height])
ps.End()