# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '/home/ee2405/ee2405/hw1/108061107.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

num_C0A880 = 0
num_C0F9A0 = 0
num_C0G640 = 0
num_C0R190 = 0
num_C0X260 = 0
tot_C0A880 = 0
tot_C0F9A0 = 0
tot_C0G640 = 0
tot_C0R190 = 0
tot_C0X260 = 0

for i in range(len(data)):
   element = data[i]
   if element['station_id'] == 'C0A880' and element['PRES'] != '-99.000' and element['PRES'] != '-999.000':
      num_C0A880 = num_C0A880 + 1
      tot_C0A880 = tot_C0A880 + float(element['PRES'])
   elif element['station_id'] == 'C0F9A0' and element['PRES'] != '-99.000' and element['PRES'] != '-999.000':
      num_C0F9A0 = num_C0F9A0 + 1
      tot_C0F9A0 = tot_C0F9A0 + float(element['PRES'])
   elif element['station_id'] == 'C0G640' and element['PRES'] != '-99.000' and element['PRES'] != '-999.000':
      num_C0G640 = num_C0G640 + 1
      tot_C0G640 = tot_C0G640 + float(element['PRES'])
   elif element['station_id'] == 'C0R190' and element['PRES'] != '-99.000' and element['PRES'] != '-999.000':
      num_C0R190 = num_C0R190 + 1
      tot_C0R190 = tot_C0R190 + float(element['PRES'])
   elif element['station_id'] == 'C0X260' and element['PRES'] != '-99.000' and element['PRES'] != '-999.000':
      num_C0X260 = num_C0X260 + 1
      tot_C0X260 = tot_C0X260 + float(element['PRES'])

if num_C0A880 != 0:
   data_C0A880 = ['C0A880', tot_C0A880 / num_C0A880]
else :
   data_C0A880 = ['C0A880', 'none']
if num_C0F9A0 != 0:
   data_C0F9A0 = ['C0F9A0', tot_C0F9A0 / num_C0F9A0]
else :
   data_C0F9A0 = ['C0F9A0', 'none']
if num_C0G640 != 0:
   data_C0G640 = ['C0G640', tot_C0G640 / num_C0G640]
else :
   data_C0G640 = ['C0G640', 'none']
if num_C0R190 != 0:
   data_C0R190 = ['C0R190', tot_C0R190 / num_C0R190]
else :
   data_C0R190 = ['C0R190', 'none']
if num_C0X260 != 0:
   data_C0X260 = ['C0X260', tot_C0X260 / num_C0X260]
else :
   data_C0X260 = ['C0X260', 'none']

target_data = [data_C0A880, data_C0F9A0, data_C0G640, data_C0R190, data_C0X260]


#=======================================


# Part. 4

#=======================================

# Print result

print(target_data)

#========================================