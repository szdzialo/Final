from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from .models import *
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
# Create your views here.
class Home(TemplateView):
        template_name = "home.html"

class QuestionCreateView(CreateView):
        model = Question
        template_name = "question/question_form.html"
        fields = ['title', 'description']
        success_url = reverse_lazy('question_list')

        def form_valid(self, form):
                form.instance.user = self.request.user
                return super(QuestionCreateView, self).form_valid(form)

class QuestionListView(ListView):
        model = Question
        template_name = "question/question_list.html"
        
class QuestionDetailView(DetailView):
        model = Question
        
class QuestionDeleteView(DeleteView):
        model = Question
        template_name = 'question/question_confirm_delete.html'
        success_url = reverse_lazy('question_list')
        template_name = 'question/question_detail.html'
        
class QuestionUpdateView(UpdateView):
        model = Question
        template_name = 'question/question_form.html'
        fields = ['title', 'description']
        
class AnswerCreateView(CreateView):
        model = Answer
        template_name = "answer/answer_form.html"
        fields = ['text']
        
        def get_success_url(self):
                return self.object.question.get_absolute_url()
        
        def form_valid(self, form):
                form.instance.user = self.request.user
                form.instance.question = Question.objects.get(id=self.kwargs['pk'])
                return super(AnswerCreateView, self).form_valid(form)