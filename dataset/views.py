from django.shortcuts import render
import textstat

# Create your views here.
def viewDataset(request):
	data = open('C:/Users/dell/Desktop/btre_project/finalYear/venv/textsequence/dataset/dataset.txt', 'r', encoding='utf-8').read()
	title = "Alice's Adventures in Wonderland, by Lewis Carroll"
	textstat.set_lang('en_US')
	print(textstat.flesch_reading_ease(data))
	context ={
	'title':title,
	'data':data
	}
	return render(request,'dataset.html',context)
