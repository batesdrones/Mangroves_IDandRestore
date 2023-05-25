import os, fnmatch
from GPSPhoto import gpsphoto
import pandas as pd
import numpy as np
import itertools


cwd = os.getcwd()


images = fnmatch.filter(os.listdir('.'), '*.jpg')

# print(images)

# image_list = os.listdir(cwd)



# def listfiles1(directory, extension):
# 	return ([f for f in os.listdir(directory) if f.endswith('.' + extension)])

# x = listfiles1(cwd, fileExt)
# print(x)




for image in images:
	
	data = gpsphoto.getGPSData(cwd + f'\\{image}')




	for keys in data.keys():
		data_keys = [data[keys]]
		keys_list_str = str(data_keys)

		# for each in keys_list_str:
		# 	lats = []
		# 	longs = []
		# 	alts = []


		opt = list(itertools.chain(data_keys))




		# print(data)
		# values = [data[keys]]
		# values = np.array(values)

		# b = values
		# print(b)



		
		# latitude = []
		# longitude = []
		# altitude = []






		# for i in range(0, len(values), 2):

		# 	latitude.append([values][i]),
		# 	longitude.append([values][i+1]),
		# 	altitude.append([values][i+2])

###this next block is in question
		# new_df = pd.DataFrame(latitude, columns=['Latitude'])
		# new_df['Longitude']
		# new_df['Altitude']

		# print(new_df)



		# print(values)



		# 	print(values)


	# 	print(data)

		# print("%s: %s" % (keys, values))






	# for key, value in data.items():
	# 	final_dict = {}

	# 	print(key)
	# 	# keys = []
		# values = str(data)[item]


		# keys.append(item)

		# print(values)
		# final_dict = {}
		# for i in x:
		# 	final_dict[i] = y[i]
		# print(final_dict)




		

		# final_dict[item] = data[][item]
		# final_dict.append(data)
		# print(final_dict)


	# keys = [[i] for i in data]
	# coords = data[image]
	# print(keys, coords)



		# keys = tag
		# values = data[tag]
		# dictionary = dict(zip(tag, values))
		# for i in keys:
		# 	dicts[i] = values[i]
		# print(dictionary)






		# print("%s: %s" %(tag, data[tag])


	# for i in data:
	# 	alt = gps.altitude
	# 	lat = gps.latitude
	# 	lon = gps.longitude
	# 	print(alt, lat, lon)
	# print(a)
	# df = pd.DataFrame.from_dict(data, orient='index')
	# print(df)


# data = gpsphoto.getGPSData('/path/to/image.jpg')
# rawData = gpsphoto.getRawData('/path/to/image.jpg')

# # Print out just GPS Data of interest
# for tag in data.keys():
#     print "%s: %s" % (tag, data[tag])

# # Print out raw GPS Data for debugging
# for tag in rawData.keys():
#     print "%s: %s" % (tag, rawData[tag])