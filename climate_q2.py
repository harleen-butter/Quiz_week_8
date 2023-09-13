import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('climate.csv')

Year = data['Year']
CO2 = data['CO2']
Temperature = data['Temperature']

plt.subplot(2, 1, 1)
plt.plot(Year, CO2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(Year, Temperature, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_2.png")

