import os
import parallelHillClimber

os.system("del world*.sdf")
os.system("del body*.urdf")
os.system("del brain*.nndf")
os.system("del fitness*.txt")
phc = parallelHillClimber.PARALLEL_HILL_CLIMBER()
phc.Evolve("DIRECT")
phc.Show_Best()
