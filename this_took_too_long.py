### RILs that didnt run

with open('RIL_list_copy.txt') as i:
	data = [list(map(str, line.strip().split(' '))) for line in i]

with open('sequenced_RILs.txt') as j:
	data2 = [list(map(str, line.strip().split('\n'))) for line in j]

[new_data] = data

flat_data2 = []
for sublist in data2:
	for item in sublist:
		flat_data2.append(item)

def diff(list1, list2):
	print(list(set(list2) ^ set(list1)))

diff(new_data, flat_data2)
