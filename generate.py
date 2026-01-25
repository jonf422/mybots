import pyrosim.pyrosim as ps

length,width,height = 1,1,1
x,y,z = 0,0,.5


ps.Start_SDF("boxes.sdf")

for i in range(10):
    ps.Send_Cube(name="Box"+str(i), pos=[x,y,z+i], size=[length-.1*i,width-.1*i,height-.1*i])
ps.End()