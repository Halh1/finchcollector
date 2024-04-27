from django.shortcuts import render, redirect

from .models import Finch, Birdhouse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches':finches
    })
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.birdhouses.all().values_list('id') 
    birdhouse_not_used = Birdhouse.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
       'finch': finch,
       'feeding_form': feeding_form,
       'birdhouses': birdhouse_not_used
    })

def assoc_birdhouse(request, finch_id, birdhouse_id):
  Finch.objects.get(id=finch_id).birdhouses.add(birdhouse_id)
  return redirect('detail', finch_id=finch_id)

def add_feeding(request, finch_id):
    submitted_form = FeedingForm(request.POST) #django version of req.body
    if submitted_form.is_valid(): 
        new_feeding = submitted_form.save(commit=False) 
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'


class FinchUpdate(UpdateView):
  model = Finch
  fields = ('breed', 'identification', 'age')


class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

class BirdhouseList(ListView):
    model = Birdhouse

class BirdhouseDetail(DetailView):
  model = Birdhouse

class BirdhouseCreate(CreateView):
  model = Birdhouse
  fields = '__all__'

class BirdhouseUpdate(UpdateView):
    model = Birdhouse
    fields = ['name', 'color']

class BirdhouseDelete(DeleteView):
  model = Birdhouse
  success_url = '/birdhouses'