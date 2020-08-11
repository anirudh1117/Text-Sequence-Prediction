from django.shortcuts import render
from django.http import HttpResponseRedirect
import docx


def index(request):
	return  render(request,'model.html')


def paper(request):
	title = "Text Sequence Prediction Using Recurrent Neural Network"
	data = readPaper()
	context ={
	'title':title,
	'data':data
	}
	return render(request,'dataset.html',context)

def readPaper():
	try:
		doc = docx.Document('C:\\Users\\dell\\Downloads\\RNN-anirudh.docx') 
		 # Creating word reader object
		data = ""
		fullText = []
		for para in doc.paragraphs:
			fullText.append(para.text)
			data = '\n'.join(fullText)

		return data
	except IOError:
		print('There was an error opening the file!')
		return None
