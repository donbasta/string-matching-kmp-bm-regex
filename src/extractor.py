from nltk import sent_tokenize
import os
import re
from kmp import kmp
from boyer_moore import boyer_moore

def convert(files_raw_data):
	
	files_raw_data = files_raw_data.replace("\n", " ")
	files_raw_data = files_raw_data.lower()
	sentences = sent_tokenize(files_raw_data)
	return sentences

def extractor(keyword, sentences, option):

	informations = []
	for sentence in sentences[1]:
		# bisa diganti dengan regex ataupun boyermoore sesuai pilihan nantinya
		if option == 'kmp':
			positions = kmp(keyword, sentence)
		elif option == 'bm':
			positions = boyer_moore(keyword, sentence)
		elif option == 'regex':
			positions = [m.start(0) for m in re.finditer(keyword, sentence)]
		if positions:
			time = find_time(sentence)
			if len(time) == 0:
				for other_sentence in sentences[1]:
					time = find_time(other_sentence)
					if time:
						break
			if len(time) == 0:
				time = ['tidak ada penanda waktu']
			amount = find_amount_info(sentence)
			closest_amount = ''
			if amount:
				closest_amount = amount[0][1]
				if len(amount) > 1:
					# find the closest one with the keyword
					minimal = len(sentence)
					for amount_candidate in amount:
						if abs(amount_candidate[0] - positions[0]) < minimal:
							closest_amount = amount_candidate[1]
							minimal = abs(amount_candidate[0] - positions[0])
			informations.append([keyword, sentences[0], time[0], closest_amount, sentence])

	return informations

def find_time(sentence):

	#currently only support date formatting
	time_pattern = re.compile(r"[0-9]{1,2}[-/][0-9]{1,2}[-/][0-9]{2,4}")
	times = time_pattern.findall(sentence)
	return times

def find_amount_info(sentence):
	amounts = [(m.start(0),m.group()) for m in re.finditer(r"[0-9]+\.*[0-9]*", sentence)]
	return amounts