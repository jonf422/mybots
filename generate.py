import pyrosim.pyrosim as ps

length,width,height = 1,1,1
x,y,z = 0,0,.5

rows, cols = 5,5

ps.Start_SDF("world.sdf")

ps.Send_Cube(name="Box",pos=[x,y,z], size=[length,width,height])
ps.End()