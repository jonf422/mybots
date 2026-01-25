import pyrosim.pyrosim as ps

length,width,height = 1,1,1
x,y,z = 0,0,.5

rows, cols = 5,5

ps.Start_SDF("boxes.sdf")

for r in range(rows):
    for c in range(cols):
        for i in range(10):
            ps.Send_Cube(name="Box"+str(r)+str(c)+str(i), 
                         pos=[x+r,y+c,z+i], 
                         size=[length-.1*i,width-.1*i,height-.1*i])
ps.End()