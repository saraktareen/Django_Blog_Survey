from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Questions
from django.urls import reverse_lazy



class QListView(ListView):
    model = Questions
    template_name = 'survey/question_list.html'

class QDetailView (DetailView):
    model = Questions
    template_name ='survey/question_detail.html'

class QCreateView (CreateView):
    model = Questions
    template_name ='survey/question_new.html'
    fields = '__all__'

class QUpdateView(UpdateView):
    model = Questions
    template_name = 'survey/question_edit.html'
    fields = ['question']

class QDeleteView(DeleteView):
    model = Questions
    template_name = 'survey/question_delete.html'
    success_url = reverse_lazy('question_list')

    