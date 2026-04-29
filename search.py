import os
import time
import parallelHillClimber

start = 10
stop = 20
for t in range(start,stop):
    try:
        os.system("del world*.sdf")
        os.system("del body*.urdf")
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del tmp*.txt")
        phc = parallelHillClimber.PARALLEL_HILL_CLIMBER()
        phc.Evolve("DIRECT", t)
        #phc.Show_Best()
        time.sleep(1)
    except PermissionError:
        t-=1
        continue

os.system(f"start /B python plotFitnessValues.py {start} {stop}")
