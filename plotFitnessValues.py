import numpy as np
import matplotlib.pyplot as plt
import sys

start = 0#int(sys.argv[1]) #start index
end = 16#int(sys.argv[2]) #end index
#range(start,end)
matrixA = np.stack([np.load(f'ABData/fitnessMatrix_A{i}.npy') for i in range(start,end+1)])
matrixB = np.stack([np.load(f'ABData/fitnessMatrix_B{i}.npy') for i in range(start,end+1)])

perRunAvgA = np.mean(matrixA, axis=1)
perRunAvgB = np.mean(matrixB, axis=1)

meanA = np.mean(perRunAvgA, axis=0)
meanB = np.mean(perRunAvgB, axis=0)
stdA  = np.std(perRunAvgA, axis=0)
stdB  = np.std(perRunAvgB, axis=0)

generations = np.arange(meanA.shape[0])


plt.figure()
for i in range(matrixA.shape[0]):
    for j in range(matrixA.shape[1]):
        plt.plot(matrixA[i, j, :], linewidth=1.0, color="blue", alpha=.6)

for i in range(matrixB.shape[0]):
    for j in range(matrixB.shape[1]):
        plt.plot(matrixB[i, j, :], linewidth=2.0, color="red", alpha=.6)

# Legend, labels, formatting
plt.plot([], [], linewidth=0.5, color="blue", alpha=0.5, label="A: Shared leg lengths")
plt.plot([], [], linewidth=2.5, color="red",  alpha=0.5, label="B: Independent leg lengths")

plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Fitness over Generations: A vs B")
plt.legend()
plt.tight_layout()
plt.savefig(f'ABData/ABTest{start}-{end}-Individual.png')
#plt.show()


plt.figure()
plt.plot(generations, meanA, linewidth=1.5, color="blue", label="A: Shared leg lengths")
plt.plot(generations, meanB, linewidth=1.5, color="red",  label="B: Independent leg lengths")
plt.fill_between(generations, meanA - stdA, meanA + stdA, color="blue", alpha=0.2, label="A: ±1 std dev")
plt.fill_between(generations, meanB - stdB, meanB + stdB, color="red",  alpha=0.2, label="B: ±1 std dev")

plt.xlabel("Generation")
plt.ylabel("Average Fitness")
plt.title(f"Average Fitness over Generations: A vs B ({end - start} runs)")
plt.legend()
plt.tight_layout()
plt.savefig(f"ABData/ABTest{start}-{end}-avg.png")
plt.show()

