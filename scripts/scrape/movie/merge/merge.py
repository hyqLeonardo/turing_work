# -*- coding: utf-8 -*-

import os

list_w = []

# lists of all characters need to be replaced
colon = [':', '：', ' ', '之', '--', ]

arabic_num = [str(n) for n in range(16)]
chinese_num = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', \
					'十一', '十二', '十三', '十四', '十五']
Roman_num = ['N', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV']
roman_num = [n.lower() for n in Roman_num]
all_num = arabic_num + chinese_num + Roman_num + roman_num
list_num = [arabic_num, chinese_num, Roman_num, roman_num]

year_num = [str(n) for n in range(1500, 3001)]

season_char = [('第%s季' % n) for n in arabic_num+chinese_num]

space_char = [',', ]

# check if already in f_w before write
def unique_w(name, f_w, list_w):
	if name not in list_w:
		list_w.append(name)
		f_w.write(name)

# replace and expand all 'colon meaning' characters with each in colon
def colon_replace(name, f_w):

	# check if has colon in name
	if sum([char in name for char in colon]) > 0:
		# find the char to replace
		for char in colon:
			if char in name:
				char_replace = char
		# replace with char in list, then write into file
		for char in colon:
			unique_w(name.replace(char_replace, char), f_w, list_w)

# helper function to replace number in different types
def expand_num(name, f_w, n, char_replace, list_other_num):
	for num in [other_list[n] for other_list in list_other_num]:
		unique_w(name.replace(char_replace, num), f_w, list_w)
		unique_w(name.replace(char_replace, ' '+num), f_w, list_w)
		unique_w(name.replace(char_replace, '('+num+')'), f_w, list_w)

# helper function, tell if a character is the last character of string
def is_last(name, char):
	return name.rindex(char) == (len(name) - 1)	# rindex finds in reverse order

# replace and expand all 'number meaning' characters
def num_replace(name, f_w):

	# don't replace if has year number
	if sum([year in name for year in year_num]) > 0:
		return
	# check if has number in name, ONLY replace first encountered type for each number 
	if sum([char in name for char in all_num]) > 0:
		# outer most loop in index of number
		for n in range(16):
			# loop in number types
			for list_n in list_num:
				# find the specific number character
				if list_n[n] in name and is_last(name, list_n[n]):
					char_replace = list_n[n]
					list_num_copy = list(list_num)	# real copy, not just reference to original list
					list_num_copy.remove(list_n)	# remove found num type
					list_other_num = list_num_copy
					expand_num(name, f_w, n, char_replace, list_other_num)
					# recrusive call funciton to add all name with number less than current
					if n > 0:
						num_replace(name.replace(char_replace, n-1))
					break
			break

def season_replace(name, f_w):

	# check if has season number in name
	if sum([s in name for s in season_char]) > 0:
		# find string to replace
		for char in season_char:
			if char in name:
				if ' '+char in name:	# if has space in front
					unique_w(name, f_w, list_w)
					unique_w(name.replace(' '+char, char), f_w, list_w)
				else:
					unique_w(name, f_w, list_w)
					unique_w(name.replace(char, ' '+char), f_w, list_w)

def expand_w(name, f_w):
	# the oder matters
	season_replace(name, f_w)
	num_replace(name, f_w)
	colon_replace(name, f_w)
					
def read_in_chunks(fd, chunck_size=1024): 
	"""Lazy function (generator) to read a file piece by piece. 
	Default chunk size: 1k. For file that is NOT line based. """
	while True:
		data = fd.read(chunck_size)
		if not data:
			break
		yield data

if __name__ == "__main__":

	# result merged file
	f_expand_w = open('merged_expand.txt', 'w')
	f_unique_w = open('merged.txt', 'w')
	# get list of all txt files in current directory
	files = [f for f in os.listdir('.') if os.path.isfile(f) and '.txt' in f]
	# process each file
	for file in files:
		'''for line based file, this method to read is already
		lazy generator'''
		print "merge file %s now ..." % file
		with open(file) as f_r:
			for name in f_r:
				# process_w(name, f_expand_w)
				unique_w(name, f_unique_w, list_w)
		f_r.close()

	f_expand_w.close()
	f_unique_w.close()
	print "all finished : )"
