# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:47:25 2019

@author: Anirudh Mittal
"""

import numpy
import sys
import keras
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dropout
from tensorflow.python.keras.layers import LSTM
from tensorflow.python.keras.callbacks import ModelCheckpoint
from tensorflow.python.keras.utils import np_utils


def generatingOutput(start):
    # load ascii text and covert to lowercase
    filename = "C:/Users/dell/Desktop/btre_project/finalYear/venv/textsequence/lstmFirst/lstm/dataset.txt"
    raw_text = open(filename, 'r', encoding='utf-8').read()
    raw_text = raw_text.lower()
    ...
    # create mapping of unique chars to integers
    chars = sorted(list(set(raw_text)))
    char_to_int = dict((c, i) for i, c in enumerate(chars))

    ...
    n_chars = len(raw_text)
    n_vocab = len(chars)
    print ("Total Characters: ", n_chars)
    print ("Total Vocab: ", n_vocab)

    ...
    # prepare the dataset of input to output pairs encoded as integers
    seq_length = 100
    dataX = []
    dataY = []
    for i in range(0, n_chars - seq_length, 1):
	    seq_in = raw_text[i:i + seq_length]
	    seq_out = raw_text[i + seq_length]
	    dataX.append([char_to_int[char] for char in seq_in])
	    dataY.append(char_to_int[seq_out])
    n_patterns = len(dataX)
    print ("Total Patterns: ", n_patterns)


    ...
    # reshape X to be [samples, time steps, features]
    X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
    # normalize
    X = X / float(n_vocab)
    # one hot encode the output variable
    y = np_utils.to_categorical(dataY)

    # define the LSTM model
    model = Sequential()
    model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
    model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    # load the network weights
    filename = "C:/Users/dell/Desktop/btre_project/finalYear/venv/textsequence/lstmFirst/lstm/weights-improvement-20-2.0818.hdf5"
    model.load_weights(filename)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    ...
    int_to_char = dict((i, c) for i, c in enumerate(chars))

    candidate = ''
    pattern = dataX[start]
    for i in range(1000):
        x = numpy.reshape(pattern, (1, len(pattern), 1))
        x = x / float(n_vocab)
        prediction = model.predict(x, verbose=0)
        index = numpy.argmax(prediction)
        result = int_to_char[index]
        candidate = candidate +result
        seq_in = [int_to_char[value] for value in pattern]
        #sys.stdout.write(result)
        pattern.append(index)
        pattern = pattern[1:len(pattern)]   
    print ("\nDone.")

    return candidate

def manualInput(input):
    filename = "C:/Users/dell/Desktop/btre_project/finalYear/venv/textsequence/lstmFirst/lstm/dataset.txt"
    raw_text = open(filename, 'r', encoding='utf-8').read()
    raw_text = raw_text.lower()
    ...
    # create mapping of unique chars to integers
    chars = sorted(list(set(raw_text)))
    char_to_int = dict((c, i) for i, c in enumerate(chars))
    input = input.lower()
    dx=[]
    for i in range(0, 1, 1):
	    seq_in = input[i:i + 100]
	    dx.append([char_to_int[char] for char in seq_in])
    
    pattern = dx[0] 
    return pattern


def generatingOutput2(pattern):
    # load ascii text and covert to lowercase
    filename = "C:/Users/dell/Desktop/btre_project/finalYear/venv/textsequence/lstmFirst/lstm/dataset.txt"
    raw_text = open(filename, 'r', encoding='utf-8').read()
    raw_text = raw_text.lower()
    ...
    # create mapping of unique chars to integers
    chars = sorted(list(set(raw_text)))
    char_to_int = dict((c, i) for i, c in enumerate(chars))

    ...
    n_chars = len(raw_text)
    n_vocab = len(chars)
    print ("Total Characters: ", n_chars)
    print ("Total Vocab: ", n_vocab)

    ...
    # prepare the dataset of input to output pairs encoded as integers
    seq_length = 100
    dataX = []
    dataY = []
    for i in range(0, n_chars - seq_length, 1):
	    seq_in = raw_text[i:i + seq_length]
	    seq_out = raw_text[i + seq_length]
	    dataX.append([char_to_int[char] for char in seq_in])
	    dataY.append(char_to_int[seq_out])
    n_patterns = len(dataX)
    print ("Total Patterns: ", n_patterns)


    ...
    # reshape X to be [samples, time steps, features]
    X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
    # normalize
    X = X / float(n_vocab)
    # one hot encode the output variable
    y = np_utils.to_categorical(dataY)

    # define the LSTM model
    model = Sequential()
    model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
    model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    # load the network weights
    filename = "C:/Users/dell/Desktop/btre_project/finalYear/venv/textsequence/lstmFirst/lstm/weights-improvement-20-2.0818.hdf5"
    model.load_weights(filename)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    ...
    int_to_char = dict((i, c) for i, c in enumerate(chars))

    candidate = ''
    for i in range(1000):
        x = numpy.reshape(pattern, (1, len(pattern), 1))
        x = x / float(n_vocab)
        prediction = model.predict(x, verbose=0)
        index = numpy.argmax(prediction)
        result = int_to_char[index]
        candidate = candidate +result
        seq_in = [int_to_char[value] for value in pattern]
        #sys.stdout.write(result)
        pattern.append(index)
        pattern = pattern[1:len(pattern)]   
    print ("\nDone.")

    return candidate


    
