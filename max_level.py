import os


directory = '1files'

max_levels = []

for i in os.listdir(directory):

	levels = []

	with open(directory + '/' + i, 'r') as file:

		lines = file.readlines()

		for j in lines:

			levels.append(j.count('?NUMBER?'))

	max_levels.append((i, max(levels)))

	print(i, max(levels))
