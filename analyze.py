import numpy as np
import matplotlib.pyplot as plt

backLeg = np.load("data/backLegSensorValues.npy")
frontLeg = np.load("data/frontLegSensorValues.npy")


plt.plot(backLeg, color="red", linewidth=3)
plt.plot(frontLeg, color="blue", linewidth=3)
plt.legend()
plt.show()
