from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from polls.models import Question, Choice
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

'''old fashion
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template("polls/index.html")
	context = {
		'latest_question_list': latest_question_list,
	}
	#output = ','.join(["%s" % (latest_question_list[i].question_text) for i in range(len(latest_question_list))])
	return HttpResponse(template.render(context)) #"Hello world, this is my first app in django, named polls!")

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, "polls/detail.html", {'question': question}) # HttpResponse("You are looking at question %s." %  question_id)

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, "polls/results.html", {'question': question})
'''

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		now = timezone.now()
		return Question.objects.filter(pub_date__lte=now).order_by('-pub_date')[:5]

class DetailView(generic.DeleteView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		:return:
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DeleteView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['selected_choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {'question': question, 'error_message':"You didn't select a choice"})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))