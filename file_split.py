with open('urqmd_catalog.txt', 'r') as file:

	lines = file.readlines()

dict = {'000077':[], '000196':[], '002000':[], '027600':[], 'new000624':[], '000115':[], '00130':[], '02760':[], '05020':[]}

for i in lines:

	split = i.split('/')

	if len(split) > 1 and split[1] in dict.keys():

		dict[split[1]].append('/'.join(split[2:]).strip())


for i in dict.keys():

	with open(i + '.txt', 'w') as wfile:

		for j in dict[i]:

			wfile.write(j + '\n')
