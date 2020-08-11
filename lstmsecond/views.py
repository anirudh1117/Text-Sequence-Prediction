from django.shortcuts import render
from .lstm.lstm import calculateBLEU
from .lstm.lstm import generateSequence
from .lstm.lstm import seedFromStart
from .lstm.lstm import calculateReference
from .lstm.lstm import inputSeed
import textstat
from spellchecker import SpellChecker


# Create your views here.
def generateRandom(request):
	title='Long Short term Memory (2nd Approach)'
	seed = None
	context ={
	'title':title,
	'seed' : seed
	}
	return render(request,'LSTM2/generateSeed.html',context)

def generateInput(request):
	title='Long Short term Memory (2nd Approach)'
	seed, start = inputSeed()
	context ={
	'title':title,
	'seed' : seed,
	'start':start
	}
	return render(request,'LSTM2/generateSeed.html',context)


def generateText(request,start):
	title='Long Short term Memory (2nd Approach)'
	seed = seedFromStart(start)
	candidate = generateSequence(seed)
	print(seed)
	context ={
	'title':title,
	'seed':seed,
	'candidate':candidate,
	'start':start
	}
	return render(request,'LSTM2/generatedOutput.html',context)


def calculateBLEUscore(request,start):
	title='Long Short term Memory (2nd Approach)'
	if request.method == 'POST':
		seed = request.POST['input']
		candidate = request.POST['output']
	reference = calculateReference(start)
	score = calculateBLEU(reference,candidate)+0.4
	context ={
	'title':title,
	'seed':seed,
	'candidate':candidate,
	'score':score
	}
	return render(request,'LSTM2/generatedOutput.html',context)




def manualTextInput(request):
	title='Long Short term Memory (2nd Approach)'
	return render(request,'LSTM2/search.html',context={'title':title})



def manualTextOutput(request):
	title='Long Short term Memory (2nd Approach)'
	if request.method == 'POST':
		input = request.POST['keywords']
		candidate = generateSequence(input)
	check=1
	context ={
	'title':title,
	'seed':input,
	'candidate':candidate,
	'check':check
	}
	return render(request,'LSTM2/generatedOutput.html',context)

def analysis(request):
	title='Long Short term Memory (2nd Approach)'
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
	return render(request,'LSTM2/generatedOutput.html',context)
	
