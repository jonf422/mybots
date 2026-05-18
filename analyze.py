import numpy as np
import matplotlib.pyplot as plt

backLeg = np.load("data/backLegSensorValues.npy")
frontLeg = np.load("data/frontLegSensorValues.npy")
fl_targetAngles = np.load("data/fl_targetAngles.npy")
bl_targetAngles = np.load("data/bl_targetAngles.npy")


plt.plot(backLeg, color="red", linewidth=4)
plt.plot(frontLeg, color="blue", linewidth=2)
plt.legend()
plt.show()

plt.plot(fl_targetAngles, color="red", linewidth=2)
plt.plot(bl_targetAngles, color='blue', linewidth=2)
plt.legend()
plt.show()
