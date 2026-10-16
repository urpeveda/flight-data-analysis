import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

DATA_FILE = "Datos de vuelo rompetechos 1.xlsx"

APOGEE = 3705
G_SCALE = 16

BARO = "MS5611_H"
# ["H331_Az", "H200_Az", "LSM_Az", "BMI_Az", "BNO_Az"]
PRI_ACCEL = "LSM_Az" # LSM_Az seems the best
G_ACCEL = "H331_Az"

def plot_line(ax, pos, label):
    ax.axvline(x=pos, color='grey', linewidth=0.7)
    ax.text(x=pos+10, y=0.97, s=label, color='grey',
            transform=ax.get_xaxis_transform(), rotation=90,
            verticalalignment='top')

df = pd.read_excel(DATA_FILE, decimal=",")

# Remove main junk data
df.loc[df[BARO] > APOGEE, BARO] = np.nan

g_condition = (df[G_ACCEL] >= 16) | (df[G_ACCEL] <= -16)
df.loc[g_condition, PRI_ACCEL] = df.loc[g_condition, G_ACCEL]

# Remove other junk data
df.loc[239:242, BARO] = np.nan
df.loc[1372, BARO] = np.nan
df.loc[3251, BARO] = np.nan

df.loc[[1551, 1554], PRI_ACCEL] = np.nan

# Create graph
ax = df.plot(y=[BARO, PRI_ACCEL], secondary_y=PRI_ACCEL)

ax.set_xlabel("Time")
ax.set_ylabel("Barometric altitude (m)")
ax.right_ax.set_ylabel("Acceleration (m/s^2)")

plot_line(ax, 83, "Liftoff")
plot_line(ax, 241, "Burnout")
plot_line(ax, 731, "Apogee")
plot_line(ax, 803, "Drogue ejection")
plot_line(ax, 3594, "Ground hit")

plt.show()