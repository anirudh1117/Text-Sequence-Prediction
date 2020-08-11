from django.urls import path

from .import views

urlpatterns = [
    path('generateSeed',views.generateRandom,name='lstm1'),
    path('generatedSeed',views.generateInput,name='lstm1.1'),
    path('generatedOutput/<int:start>',views.generateText,name='lstm1.2'),
    path('Output/<int:start>',views.calculateBLEUscore,name='lstm1.3'),
    path('search',views.manualTextInput,name='search1'),
    path('Output',views.manualTextOutput,name='lstm1.4'),
    path('Output-analysis',views.analysis,name='lstm1.5'),
    ]