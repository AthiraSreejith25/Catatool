#!/usr/bin/python3.8

import os
import re

target = 'files/syntheticdata_catalog.txt'

with open(target, 'r') as rfile:

	lines = rfile.readlines()

wfile = open('catatool_{}.out'.format(target.split('/')[1]), 'w')


cmd1 = '''awk '{gsub(/[0-9]+/, "?NUMBER?"); print}' %s | sort -u''' % target
out1 = os.popen(cmd1).read()

#print(out1)
patterns = out1.split('\n')


no_num = []
#num = []


for nth in range(len(patterns)):

	print(patterns[nth])


	if '?NUMBER?' not in patterns[nth]:


		no_num.append(patterns[nth])


	else:


		pattern = patterns[nth].replace('?NUMBER?', '[0-9]+')
		num_count = patterns[nth].count('?NUMBER?')
		num_sets = [set() for i in range(num_count)]

		count = 0
		number = re.compile('[0-9]+')

		matches = [[] for i in range(num_count)]


		for i in lines:

			if re.search(pattern, i):

				count += 1
				matches[0].append(i)

				m = re.search('[0-9]+', i)

				num_sets[0].add(m.group())

		k = sorted(num_sets[0], key = int)
		pattern_split = patterns[nth].split('?NUMBER?')

		if len(num_sets[0]) < 5:

			text = '\n'.join([pattern_split[0] + str(i) for i in k])

			wfile.write(text + '\n\n')

		else:


			text = pattern_split[0] + str(k[0]) + '\n' + pattern_split[0] + str(k[1]) + '\n.\n. {} instances\n.\n'.format(len(num_sets[0])) + pattern_split[0] + str(k[-2]) + '\n' + pattern_split[0] + str(k[-1])

			wfile.write(text + '\n\n')


		if num_count > 1:

			cc = -1
			num_sets[0] = sorted(num_sets[0], key = int)

			for i in num_sets[0]:

				cc += 1
				matches[1] = [[] for kk in range(len(num_sets[0]))]
				num_sets[1] = [set() for kk in range(len(num_sets[0]))]

				for j in matches[0]:

					if re.search(pattern_split[0] + str(i), j):

						matches[1][cc].append(j)
						num_sets[1][cc].add(number.findall(j)[1])


				k = sorted(num_sets[1][cc], key = int)
				pattern_1 = pattern_split[0] + str(i) + pattern_split[1]


				if len(num_sets[1][cc]) < 5:

					text = '\n'.join([pattern_1 + str(i) for i in k])

					wfile.write(text + '\n\n')

				else:

					text = pattern_1 + str(k[0]) + '\n' + pattern_1 + str(k[1]) + '\n.\n. {} instances\n.\n'.format(len(num_sets[1][cc])) + pattern_1 + str(k[-2]) + '\n' + pattern_1 + str(k[-1]) + '\n'

					wfile.write(text +'\n\n')


wfile.write('\n\n\n')
wfile.write('\n'.join(no_num))


#if num_count > 2:

#	for i in num_sets


#print(num_count)
#print(count)

wfile.close()

'''
for pattern in patterns:

	if '?NUMBER?' in pattern:

		pass



	else:

		no_num.append(pattern)


#print((lines))

with open('catatool.out', 'w') as wfile:

	wfile.write('\n'.join(no_num))
	wfile.write('\n\n\n')
'''
