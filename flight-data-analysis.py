import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

DATA_FILE = "Datos de vuelo rompetechos 1.xlsx"

APOGEE = 3705

df = pd.read_excel(DATA_FILE, decimal = ",")

for row in df.index:
    #df.loc[row, "ulFTime"] = row # Renumber x axis

    if df.loc[row, "MS5611_H"] > APOGEE: # Remove main junk data
        df.loc[row, "MS5611_H"] = np.nan

    if df.loc[row, "BMP581_P"] == 0:
        df.loc[row, "BMP581_P"] = np.nan

# Remove other junk data
df.loc[239:242, "MS5611_H"] = np.nan
df.loc[1372, "MS5611_H"] = np.nan
df.loc[3251, "MS5611_H"] = np.nan

df.plot(y = "MS5611_H")
#df.plot(y = [], secondary_y=True, ax = ax)

plt.show()