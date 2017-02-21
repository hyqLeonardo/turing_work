# -*- coding: utf-8 -*-

import os
import sys

import pdb

CHINESE_NUM_LEN = 3
ARABIC_NUM_LEN = 1

# lists of all characters need to be replaced
# colon = [':', '：', ' ', '之']
colon = [':', '：']

arabic_num = [str(n) for n in range(16)]
chinese_num = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', \
					'十一', '十二', '十三', '十四', '十五']
Roman_num = ['N', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV']
roman_num = [n.lower() for n in Roman_num]
all_num = arabic_num + chinese_num + Roman_num + roman_num
list_num_all = [arabic_num, chinese_num, Roman_num, roman_num]

year_num = [str(n) for n in range(1500, 3001)]

season_char = [('第%s季' % n) for n in arabic_num+chinese_num] + \
				[('第%s部' % n) for n in arabic_num+chinese_num]

### Common helper functions

# check if already in record before write
def unique_record(name_list, record, verbose=False):
	for name in name_list:
		if name not in record:
			if type(record) is dict:	# tell type of record
				record[name] = None
			elif type(record) is list:
				record.append(name)
		elif verbose == True:
			print 'repeated name %s' % name

# fucntion template to call other replace functions
def replace_record(replace_func, args, record):
	unique_record(replace_func(*args), record)

# helper function to get the number
def get_num_type(char, list_num=list_num_all):
	for l in list_num:
		for n in range(len(l)):
			if l[n] in char:
				return (n, l)

# write all item in record into file f_w
def write_record(f_w, record):
	for name in record:
		name_no_space = "".join(name.split())
		f_w.write(name_no_space + '\n')

### Colon

# replace and expand all 'colon meaning' characters with each in colon
def colon_replace(name):

	result = []
	# check if has colon in name
	if sum([char in name for char in colon]) <= 0:	# if doesn't have, write unmodified
		return [name]
	# find the char to replace
	for char in colon:
		if char in name:
			char_replace = char
	# replace with char in list, then write into file
	for char in colon:
		result.append(name.replace(char_replace, char))

	return result

def colon_replace_record(name, record):
	'''do NOT remove the ',' in (name, ), or *args won't be able to 
		unwrap this as a tuple, instead unwrap the string'''
	replace_record(colon_replace, (name, ), record)

### Number 

# helper function, tell if a character is the last character of string
def is_last(name, char):
	if name[-1] != '\n':	# last char is not '\n'
		if len(char) == CHINESE_NUM_LEN:	# chinese number
			return name.rindex(char) == (len(name) - CHINESE_NUM_LEN)	# rindex() finds in reverse order
		elif len(char) == ARABIC_NUM_LEN:	# arabic number
			return name.rindex(char) == (len(name) - ARABIC_NUM_LEN)
	else:
		if len(char) == CHINESE_NUM_LEN:	# chinese number
			return name.rindex(char) == (len(name) - (CHINESE_NUM_LEN+1))	# rindex() finds in reverse order
		elif len(char) == ARABIC_NUM_LEN:	# arabic number
			return name.rindex(char) == (len(name) - (ARABIC_NUM_LEN+1))


# helper function to replace number in different types
def expand_num(name, n, char_replace, list_number, verbose=False):
	result = list()
	for num in [list_n[n] for list_n in list_number]:
		result.append(name.replace(char_replace, num))
		# result.append(name.replace(char_replace, ' '+num))
		# result.append(name.replace(char_replace, '('+num+')'))
	return result

# replace and expand all 'number meaning' characters
def num_replace(name, list_number):

	# don't replace if has year number
	if sum([year in name for year in year_num]) > 0:
		return [name]
	if sum([char in name for char in all_num]) <= 0:
		return [name]

	(n, list_n) = get_num_type(name)
	# ONLY replace if it's the last character
	if is_last(name, list_n[n]):
		char_replace = list_n[n]
		num_result = expand_num(name, n, char_replace, list_number)
	else:
		return [name]

	return num_result

def num_replace_record(name, record):
	list_number = [arabic_num, chinese_num]
	replace_record(num_replace, (name, list_number), record)

'''recursively replace and expand all 'number meaning' characters, 
	implemented by callback function, 
	num_recursive_record -> num_recursive -> num_recursive_record'''
def num_recursive(name, list_number, num_result=list()):

	# don't replace if has year number
	if sum([year in name for year in year_num]) > 0:
		return [name]
	if sum([char in name for char in all_num]) <= 0:
		return [name]

	(n, list_n) = get_num_type(name)
	# ONLY replace if it's the last character
	if is_last(name, list_n[n]):
		char_replace = list_n[n]
		num_result.extend(expand_num(name, n, char_replace, list_number))	# expand current
		if n > 1:	# recursively expand with number less than current, bigger than 1
			recur_name = name.replace(char_replace, list_n[n-1])	# decrease 1
			num_recursive(recur_name, list_number, num_result)	
	else:
		return [name]

	return num_result

def num_recursive_record(name, record):
	list_number = [arabic_num, chinese_num]
	replace_record(num_recursive, (name, list_number), record)


### Season

# replace and expand season phrase
def season_replace(name, record, recursive=False):

	season_result = list()
	list_season_num = [arabic_num, chinese_num]
	# check if has season number in name
	if sum([s in name for s in season_char]) <= 0:
		return [name]

	# find string to replace
	char_replace = str()
	for char in season_char:
		if char in name:
			char_replace = char
			break

	# break into 2 parts, then use num_replace()
	first_part = str()
	second_part = str()
	if len(char_replace) == 9:	# middle number is in chinese
		first_part = char_replace[:6]
		second_part = char_replace[6:]
	elif len(char_replace) == 7:	# middle number is in arabic
		first_part = char_replace[:4]
		second_part = char_replace[4:]
	list_num_a_c = [arabic_num, chinese_num]
	if recursive == False:	# no recursively expand
		replace_part_list = num_replace(first_part, list_num_a_c)
	else:	# recursively expand, use num_recursive
		replace_part_list = num_recursive(first_part, list_num_a_c)
	replace_list = [first + second_part for first in replace_part_list]

	# expand space
	for r in replace_list:
		season_result.append(name.replace(char, r))

	return season_result

def season_replace_record(name, record):
	'''do NOT remove the ',' in (name, ), or *args won't be able to 
		unwrap this as a tuple, instead unwrap the string'''
	replace_record(season_replace, (name, record, False), record)
	num_result = list()
	season_result = list()

def season_recursive_record(name, record):
	'''do NOT remove the ',' in (name, ), or *args won't be able to 
		unwrap this as a tuple, instead unwrap the string'''
	replace_record(season_replace, (name, record, True), record)
	num_result = list()
	season_result = list()

### Overall

# expand all avaliable chars
def expand_record(name, record):
	season_replace_record(name, record)
	num_replace_record(name, record)
	colon_replace_record(name, record)

# expand with recursive number replace
def recursive_expand_record(name, record):
	season_recursive_record(name, record)
	num_recursive_record(name, record)
	colon_replace_record(name, record)


### Main routine 

def main():

	# modify this to change storage data structure
	list_record = list() 
	dict_record = dict()
	record = dict_record
	# result merged file
	f_recursive_expand_w = open('merged_recursive', 'w')
	f_expand_w = open('merged_expand', 'w')
	f_unique_w = open('merged', 'w')
	# get list of all txt files in current directory
	files = [f for f in os.listdir('.') if os.path.isfile(f) and '.txt' in f]
	# process each file
	for file in files:
		'''for line based file, this method to read is already
		lazy generator'''
		print "merge file %s now, with a dict of length %i, %i bytes" \
				%(file, len(record), sys.getsizeof(record))
		with open(file) as f_r:
			for name in f_r:
				recursive_expand_record(name, record)
				# expand_record(name, record)
				# unique_record([name], record)
		f_r.close()

	write_record(f_recursive_expand_w, record)
	f_recursive_expand_w.close()
	# write_record(f_expand_w, record)
	f_expand_w.close()
	# write_record(f_unique_record, record)
	f_unique_w.close()

	print "all finished : )"

### Test routines

# test by one line 
def test_line():

	# modify this to change storage data structure
	# list_record = list() 
	dict_record = dict()
	record = dict_record
	# setup
	line = '少年师爷第9季'
	test_w = open('test', 'w')
	# print result	
	list_number = [arabic_num, chinese_num]
	# res = num_replace(line, list_number)
	# res = num_recursive(line, list_number)
	# res = colon_replace(line)
	# res = season_replace(line)
	res = season_replace(line, record, True)
	for i in range(len(res)):
		print res[i]
	# write result
	# expand_record(line, test_w, record)
	recursive_expand_record(line, record)
	write_record(test_w, record)
	test_w.close()

# test by one file
def test_file():

	# modify this to change storage data structure
	list_record = list() 
	dict_record = dict()
	record = dict_record
	# file setup
	f_unique_w = open('merged_test', 'w')
	f_expand_w = open('merged_expand_test', 'w')
	f_recursive_w = open('merged_recursive_test', 'w')

	count_lines = 0
	file = 'file_for_test'
	with open(file) as f_r:
		for name in f_r:
			count_lines += 1
			# name = "".join(name.split())	# remove all white spaces
			# unique_record([name], f_unique_record, record, verbose=False)
			# expand_record(name, record)
			recursive_expand_record(name, record)

	f_r.close()
	# write_record(f_unique_w, record)
	f_unique_w.close()
	# write_record(f_expand_w, record)
	f_expand_w.close()
	write_record(f_recursive_w, record)
	f_recursive_w.close()

	print 'totally %i lines in file %s, %i keys in record with size of %i bytes' \
			%(count_lines, file, len(record), sys.getsizeof(record))


if __name__ == "__main__":

	# main()
	# test_line()
	test_file()

