import json

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy

from . import models

def save(request, pk):
	table = get_object_or_404(models.Table, id=pk)
	table.fields = request.POST.get('fields', [])
	table.save()
	return HttpResponse('200 OK')

class Index(generic.ListView):
	model=models.Table

class Detail(generic.DetailView):
	model=models.Table

class Create(generic.CreateView):
	model=models.Table
	fields=['name']

class Delete(generic.DeleteView):
	model=models.Table
	success_url=reverse_lazy('table_index')

class Update(generic.UpdateView):
	model=models.Table
	fields=['name']
