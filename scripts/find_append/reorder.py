import re

fname_std = "q_std_new.txt"
fname_find = "q_find_new.txt"
f_w = open('append_new.txt', 'w')

with open(fname_std) as f1:
   	 content1 = f1.readlines()

with open(fname_find) as f2:
	content2 = f2.readlines()

for std in content1:
	flag = 0
	std_split = std.split("\t", 1)
	for find in content2:
		find_split = find.split("\t", 1)
		if find_split[0] == std_split[0]:
			flag = 1
			if (std_split[1] != ""):
				combined = std[:-1] + '\t' + find_split[1]
			else:
				combined = std[:-1] + '\t' + '\t' + find_split[1]
			f_w.write(combined)
			break
	if flag == 0:
		f_w.write(std)

print("finished")

f_w.close()
