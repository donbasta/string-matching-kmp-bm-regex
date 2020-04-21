from nltk import sent_tokenize
import assets
import os
import re
from kmp import kmp
from boyer_moore import boyer_moore

directory = os.getcwd() + '/textfile'
news = []

for file in os.listdir(directory):
	with open('/'.join((directory,file)), "r") as textfile: 
		text = textfile.read().replace("\n", " ")
		text = text.lower()
		sentences = sent_tokenize(text)
		news.append(sentences)

def extract(keyword, sentences):

	informations = []
	for sentence in sentences:
		# bisa diganti dengan regex ataupun boyermoore sesuai pilihan nantinya
		positions = kmp(keyword, sentence)
		if positions:
			time = find_time(sentence)
			amount = find_amount_info(sentence)
			informations.append([keyword, time, amount, sentence])

	return informations

def find_time(sentence):
	time_pattern = re.compile(r"[0-9]{2}[-/][0-9]{2}[-/][0-9]{2,4}")
	times = time_pattern.findall(sentence)
	return times

def find_amount_info(sentence):
	amounts = re.findall(r"[0-9]+", sentence)
	return amounts

def create_results(info):
	return f"Keyword: {info[0]}\nHasil Ekstraksi Informasi:\nJumlah: {info[2]}\nWaktu: {info[1]}\n{info[3]}"

def results(keyword):

	informations = []

	for sentences in news:
		informations += extract(keyword, sentences)

	for information in informations:
		print(create_results(information))

if __name__ == "__main__":
	keyword = input()
	results(keyword.lower())





