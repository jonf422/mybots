import numpy as np
import matplotlib.pyplot as plt

matrixA = np.load('fitnessMatrix_A.npy')
matrixB = np.load('fitnessMatrix_B.npy')

plt.figure()
for i in range(matrixA.shape[0]):
    plt.plot(matrixA[i, :], linewidth=1.0, color="blue", alpha=.8)

for i in range(matrixB.shape[0]):
    plt.plot(matrixB[i, :], linewidth=2.5, color="red", alpha=.8)

# Legend, labels, formatting
plt.plot([], [], linewidth=0.5, color="blue", alpha=0.5, label="A: Shared leg lengths")
plt.plot([], [], linewidth=2.5, color="red",  alpha=0.5, label="B: Independent leg lengths")

plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Fitness over Generations: A vs B")
plt.legend()
plt.tight_layout()
#plt.show()

avgA = np.mean(matrixA, axis=0)
avgB = np.mean(matrixB, axis=0)

stdA = np.std(matrixA, axis=0)
stdB = np.std(matrixB, axis=0)

generations = np.arange(avgA.shape[0])

plt.figure()
plt.plot(generations, avgA, linewidth=1.5, color="blue", label="A: Shared leg lengths")
plt.plot(generations, avgB, linewidth=1.5, color="red",  label="B: Independent leg lengths")

plt.fill_between(generations, avgA - stdA, avgA + stdA, color="blue", alpha=0.2, label="A: ±1 std dev")
plt.fill_between(generations, avgB - stdB, avgB + stdB, color="red",  alpha=0.2, label="B: ±1 std dev")

plt.xlabel("Generation")
plt.ylabel("Average Fitness")
plt.title("Average Fitness over Generations: A vs B")
plt.legend()
plt.tight_layout()
plt.show()