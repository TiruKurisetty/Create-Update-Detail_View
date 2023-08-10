from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,CreateView,UpdateView,DetailView


class School_list(ListView):
    model=School
    context_object_name='allO'

class School_detail(DetailView):
    model=School
    context_object_name='schoolD'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
