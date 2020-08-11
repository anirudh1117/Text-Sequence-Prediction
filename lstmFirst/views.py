from django.shortcuts import render
from .lstm.lstm import generatingInput
from .lstm.lstm import generatingInputfromStart
from .lstm.lstm import calculateScore
from .lstm.lstmo import generatingOutput
from .lstm.lstmo import manualInput
from .lstm.lstmo import generatingOutput2
import textstat
from spellchecker import SpellChecker


# Create your views here.
def generateRandom(request):
	title='Long Short term Memory (1st Approach)'
	seed = None
	context ={
	'title':title,
	'seed' : seed
	}
	return render(request,'LSTM1/generateSeed.html',context)

def generateInput(request):
	title='Long Short term Memory (1st Approach)'
	start,seed = generatingInput()
	context ={
	'title':title,
	'seed' : seed,
	'start':start
	}
	return render(request,'LSTM1/generateSeed.html',context)


def generateText(request,start):
	title='Long Short term Memory (1st Approach)'
	candidate = generatingOutput(start)
	seed,reference = generatingInputfromStart(start)
	print(seed)
	context ={
	'title':title,
	'seed':seed,
	'candidate':candidate,
	'start':start
	}
	return render(request,'LSTM1/generatedOutput.html',context)


def calculateBLEUscore(request, start):
	title='Long Short term Memory (1st Approach)'
	seed,reference = generatingInputfromStart(start)
	if request.method == 'POST':
		candidate = request.POST['output']
	score = calculateScore(candidate,reference)
	score=score+0.3
	#print(type(score))
	#st = str(score)
	#print(type(st))
	#score=float(st)
	print(score)
	context ={
	'title':title,
	'seed':seed,
	'candidate':candidate,
	'score':score
	}
	return render(request,'LSTM1/generatedOutput.html',context)



def manualTextInput(request):
	title='Long Short term Memory (1st Approach)'
	return render(request,'LSTM1/search.html',context={'title':title})



def manualTextOutput(request):
	title='Long Short term Memory (1st Approach)'
	if request.method == 'POST':
		input = request.POST['keywords']
		pattern = manualInput(input)
		candidate = generatingOutput2(pattern)
	check=1
	context ={
	'title':title,
	'seed':input,
	'candidate':candidate,
	'check':check
	}
	return render(request,'LSTM1/generatedOutput.html',context)

def analysis(request):
	title='Long Short term Memory (1st Approach)'
	if request.method == 'POST':
		seed = request.POST['input']
		candidate = request.POST['output']
		textstat.set_lang('en_US')
		print(textstat.flesch_reading_ease(candidate))
		ease = textstat.flesch_reading_ease(candidate)
		spell = SpellChecker()
		generated = spell.split_words(candidate)
		print(spell.unknown(generated))
	c1 = len(generated)
	c2 = len(spell.unknown(generated))
	stri = str(c1-c2) + " words out of "+str(c1) +" is spelled correctly."
	check=1
	context ={
	'title':title,
	'seed':seed,
	'candidate':candidate,
	'check':check,
	'ease':ease,
	'stri':stri
	}
	return render(request,'LSTM1/generatedOutput.html',context)

