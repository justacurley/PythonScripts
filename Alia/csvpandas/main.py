# aset = []
# with open("weather_data.csv") as csv:
#     for line in csv.readlines():
#         aset.append(line)
# print(aset)

# import csv
# temps = []
# with open("weather_data.csv") as data:
#     rows = csv.reader(data)
#     next(rows)
#     for row in rows:
#         temps.append(int(row[1]))
# print(temps)

import pandas
# data=pandas.read_csv("weather_data.csv")
# # convert to dataset to dict
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()

# # print(data["temp"].mean())
# # print("maxtemp",data["temp"].max())

# # Get Data in column
# # print(data.temp)

# # Get data in rows
# maxtemp = data["temp"].max()
# # print(data[data.temp == maxtemp])

# monday = data[data.day == "Monday"]
# ftemp = (int(monday.temp) * 9/5) + 32
# # print(ftemp)

# # create dataframe from scratch
# datadict = {
#     "students":["alex","alia"],
#     "scores":[98,99]
# }
# data = pandas.DataFrame(datadict)
# data.to_csv("new_data.csv")

# Primary Fur Color
# Figure out totals of each squirel color, put that into a new dataframe and create a csv

data = pandas.read_csv("sqdata.csv")
(data["Primary Fur Color"].value_counts(dropna=False)).to_csv("colors.csv")
