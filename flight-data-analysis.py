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

ax.axvline(x=83, color='grey', linewidth=0.7)
ax.text(x=83+10, y=0.97, s='Liftoff', color='grey', 
        transform=ax.get_xaxis_transform(), 
        rotation=90,
        verticalalignment='top')

ax.axvline(x=241, color='grey', linewidth=0.7)
ax.text(x=241+10, y=0.97, s='Burnout', color='grey', 
        transform=ax.get_xaxis_transform(), 
        rotation=90,
        verticalalignment='top')

ax.axvline(x=731, color='grey', linewidth=0.7)
ax.text(x=731+10, y=0.97, s='Apogee', color='grey', 
        transform=ax.get_xaxis_transform(), 
        rotation=90,
        verticalalignment='top')

ax.axvline(x=803, color='grey', linewidth=0.7)
ax.text(x=803+10, y=0.97, s='Drogue ejection', color='grey', 
        transform=ax.get_xaxis_transform(), 
        rotation=90,
        verticalalignment='top')

ax.axvline(x=803, color='grey', linewidth=0.7)
ax.text(x=803+10, y=0.97, s='Drogue ejection', color='grey', 
        transform=ax.get_xaxis_transform(), 
        rotation=90,
        verticalalignment='top')

ax.axvline(x=3594, color='grey', linewidth=0.7)
ax.text(x=3594+10, y=0.97, s='Ground hit', color='grey', 
        transform=ax.get_xaxis_transform(), 
        rotation=90,
        verticalalignment='top')

plt.show()