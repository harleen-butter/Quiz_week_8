import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")
data = cursor.fetchall()

Year = [row[0] for row in data]
CO2 = [row[1] for row in data]
Temperature = [row[2] for row in data]

conn.close()

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
plt.savefig("co2_temp_1.png")


