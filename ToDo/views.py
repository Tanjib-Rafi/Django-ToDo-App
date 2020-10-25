from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .models import Todo
from .forms import TodoForm

# Create your views here.

def index(request):
    todos= Todo.objects.all()

    form = TodoForm()

    if request.method=='POST':
         form = TodoForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/')

    context = {'todos' : todos, 'form' : form}
    return render(request,'ToDo/list.html',context)

def update(request, pk):
    todo = Todo.objects.get(id=pk)

    form=TodoForm(instance=todo)

    if request.method=='POST' :
        form=TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('/')



    context = {'form' : form}

    return render(request,'ToDo/update.html',context)

def delete(request,pk):
    delete = Todo.objects.get(id=pk)

    if request.method =='POST':
        delete.delete()
        return redirect('/')


    context = {'delete' : delete}
    return render(request, 'Todo/delete.html',context)