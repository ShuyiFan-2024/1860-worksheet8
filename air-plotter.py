import matplotlib.pyplot as pyplot
import pandas as pd

air_data=pd.read_csv("leeds-centre-air-quality.csv")
air_data["avg"]=(air_data["pm25"]+air_data["pm10"]+air_data["o3"]+air_data["no2"])/4
air_data=air_data["avg"]
al=air_data.plot(kind="line")
al.set_xticks(air_data.index)
pyplot.show()