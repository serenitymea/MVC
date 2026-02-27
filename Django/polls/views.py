from django.shortcuts import render
from .models import Question
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(question.question_text)