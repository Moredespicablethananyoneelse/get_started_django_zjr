from django.shortcuts import render

# Create your views here.

# coded by me  Writing your first Django app,part 2 
#from django.http import HttpResponse
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

# coded by me Wring your first Django app, part 3
from .models import Question
from django.http import HttpResponse
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)



# coded by me Writing your first Django app, part 1
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id);


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)