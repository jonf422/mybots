import pyrosim.pyrosim as ps

length,width,height = 1,1,1
x,y,z = 0,0,.5


ps.Start_SDF("boxes.sdf")
ps.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
ps.Send_Cube(name="Box2", pos=[x+1,y,z+1], size=[length,width,height])
ps.End()