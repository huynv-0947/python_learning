from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Question, Choice

def index(request):
  questions = Question.objects.order_by('-publish_date')[:5]
  template = loader.get_template('polls/index.html')
  context = {
    'questions': questions,
  }
  return HttpResponse(template.render(context, request))

def detail(request, question_id):
  try:
    question = Question.objects.get(id = question_id)
  except Question.DoesNotExist:
    raise Http404('Question %s not exist!' % question_id)

  return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
  question = get_object_or_404(Question, id = question_id)
  return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
  question = get_object_or_404(Question, id = question_id)
  try:
    selected_choice = question.choice_set.get(id = request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice.",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
