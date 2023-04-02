from django.shortcuts import get_object_or_404, render,redirect
from .models import Task
from .forms import TaskForm
import pdb
from django.http import HttpResponse
from django.views.decorators.debug import sensitive_variables
from django.http import HttpResponseNotFound,HttpResponseBadRequest
from django.db import connection
from django.db.models import Q
# Create your views here.


def index(request):
    welcome = 'WELCOME TO TODO APP'
    getallList = Task.objects.all()
    title = "UPDATE STATUS"
    context = {
        'title':welcome,
        'task':getallList,
        'form':title
        }
    return render(request, 'todolist/index.html', context)
def update(request,id):
    with connection.cursor() as cursor:
        cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
        task = get_object_or_404(Task, id=id)
        getallList = Task.objects.all()
        title = 'UPDATE'
        if request.method == 'POST':
            status = request.POST.get('status')
            task.status = bool(int(status))
            task.save()
            return redirect('todolist:index')
        context = {
            'title':title,
            'task':getallList,
            'taskid':task
        }
        return render(request,'todolist/update.html',context)
def updateStatus(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        # Handle case where Task with id=id doesn't exist
        return HttpResponseNotFound()

    if request.method == 'POST':
        status = request.POST.get('status')
        try:
            bool_status = bool(int(status))
        except ValueError:
            # Handle case where status is not a valid integer
            return HttpResponseBadRequest()

        task.status = bool_status
        task.save()
    return redirect('todolist:index')
def delete(request,id):
    task = get_object_or_404(Task,id=id)
    task.delete()
    return redirect('todolist:index')

def addTask(request):
        if request.method == 'POST':
            task_name = request.POST.get('task_name')
            task = Task(task_name=task_name, status=False)
            task.save()
        else:
            return HttpResponseBadRequest()
        return redirect('todolist:index')

def searchResult(request):
    getallList = Task.objects.all()
    query = request.GET.get('q')
    if query.isdigit() ==True:
        results = Task.objects.filter(Q(id=query))
    else:
        results = Task.objects.filter(Q(status=query))
    if not results:
        results = getallList
    context = {'task': results}
    return render(request, 'todolist/index.html', context)