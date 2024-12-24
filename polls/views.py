from django.shortcuts import render

from django.http import Http404
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Choice
# Create your views here.

# coded by me  Writing your first Django app,part 2 
#from django.http import HttpResponse
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

# coded by me Wring your first Django app, part 3
#from .models import Question
#from django.http import HttpResponse
#def index(request):
#    latest_question_list = Question.objects.order_by("-pub_date")[:5]
#    output = ", ".join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

#coded by me Writing your first Django app, part3
from .models import Question
from django.http import HttpResponse
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list" : latest_question_list,
    }
    return HttpResponse(template.render(context, request))


# coded by me Writing your first Django app, part 3
#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id);

# coded by me Writing your first Django app, part 3

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

## coded by me Writing your first Django app, part 3
#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)
# coded by me Wrting your first Django app, part 4
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/results.html", {"question": question})

# coded by me Writing your first Django app, part 3
#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)

#coded by me Writing your first Django app, part4

def vote(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
            "question": question,
            "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))