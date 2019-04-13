
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView, TemplateView,
                                  RedirectView)
from blog import models


from django.shortcuts import render
from django.http import HttpResponse

class JokeCreateView(CreateView):
    model = models.Jokes
    template_name = 'joke_form.html'
    fields = ('joke_title', 'joke')

class JokeListView(ListView):
    model = models.Jokes
    template_name = 'joke_list.html'

def index(request):
    return HttpResponse("<b>Hello World</b>")
def get_post(request, id):
    return HttpResponse("Post #{}".format(id))
def greet(request, name):
    return HttpResponse("Hello {}".format(name))
