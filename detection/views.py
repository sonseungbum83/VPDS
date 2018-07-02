from django.shortcuts import render
from django.http import HttpResponse
from detection import tests
from django.template import loader
from .models import Question

def main(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('main/main.html')
    context = {
        'latest_question_list': latest_question_list,
    }    
    return HttpResponse(template.render(context, request))

def test(request):
    tests.insert_question()
    return HttpResponse("Test done.")
