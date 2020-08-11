# -*- coding: utf-8 -*-
"""
Created on Thu April 25 23:28:46 2020

@author: Anirudh Mittal
"""

from random import randint
from pickle import load
from tensorflow.python.keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from nltk.translate.bleu_score import sentence_bleu

# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

# generate a sequence from a language model
def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
	result = list()
	in_text = seed_text
	# generate a fixed number of words
	for _ in range(n_words):
		# encode the text as integer
		encoded = tokenizer.texts_to_sequences([in_text])[0]
		# truncate sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
		# predict probabilities for each word
		yhat = model.predict_classes(encoded, verbose=0)
		# map predicted word index to word
		out_word = ''
		for word, index in tokenizer.word_index.items():
			if index == yhat:
				out_word = word
				break
		# append to input
		in_text += ' ' + out_word
		result.append(out_word)
	return ' '.join(result)


def inputSeed():
    in_filename = 'C:/Users\dell/Desktop/btre_project/finalYear/venv/textsequence/lstmsecond/lstm/republic_sequences.txt'
    doc = load_doc(in_filename)
    lines = doc.split('\n')
    start = randint(0,len(lines))
    seed_text = lines[start]
    #print(seed_text + '\n')
    #print(len(seed_text))
    return seed_text,start

def seedFromStart(start):
    in_filename = 'C:/Users\dell/Desktop/btre_project/finalYear/venv/textsequence/lstmsecond/lstm/republic_sequences.txt'
    doc = load_doc(in_filename)
    lines = doc.split('\n')
    seed_text = lines[start]
    return seed_text

def generateSequence(seed_text):
    in_filename = 'C:/Users\dell/Desktop/btre_project/finalYear/venv/textsequence/lstmsecond/lstm/republic_sequences.txt'
    doc = load_doc(in_filename)
    lines = doc.split('\n')
    seq_length = len(lines[0].split()) - 1

    # load the model
    model = load_model('C:/Users\dell/Desktop/btre_project/finalYear/venv/textsequence/lstmsecond/lstm/model.h5')

    # load the tokenizer
    tokenizer = load(open('C:/Users\dell/Desktop/btre_project/finalYear/venv/textsequence/lstmsecond/lstm/tokenizer.pkl', 'rb'))

    #load input
    #seed_text = lines[start]

    candidate = generate_seq(model, tokenizer, seq_length, seed_text, 100)

    return candidate

def calculateReference(start):
    in_filename = 'C:/Users\dell/Desktop/btre_project/finalYear/venv/textsequence/lstmsecond/lstm/republic_sequences.txt'
    doc = load_doc(in_filename)
    lines = doc.split('\n')
    reference = lines[start+51] + lines[start+101]
    return reference


def calculateBLEU(reference,candidate):
    from nltk.translate.bleu_score import SmoothingFunction
    smoothie = SmoothingFunction().method4
    score = sentence_bleu(reference, candidate,smoothing_function=smoothie)
    return score

