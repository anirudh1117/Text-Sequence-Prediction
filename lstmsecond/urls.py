from django.urls import path

from .import views

urlpatterns = [
    path('generateSeed',views.generateRandom,name='lstm2'),
    path('generatedSeed',views.generateInput,name='lstm2.1'),
    path('generatedOutput/<int:start>',views.generateText,name='lstm2.2'),
    path('Output/<int:start>',views.calculateBLEUscore,name='lstm2.3'),
    path('search',views.manualTextInput,name='search'),
    path('Output',views.manualTextOutput,name='lstm2.4'),
    path('Output-analysis',views.analysis,name='lstm2.5'),
    ]