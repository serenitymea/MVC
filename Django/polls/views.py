from .models import Question
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(question.question_text)