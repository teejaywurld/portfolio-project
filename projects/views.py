from django import forms
from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project
from django.contrib import messages


def small_project(request):
    return render(request, 'small_project.html', {})


def create_project(request):
    data = request.POST
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(data=data)
        title = data.get('title')
        if form.is_valid() and data.get('technology') != "person":
            form.save()
            messages.success(request, f"{title} just got created")
            return redirect('view_all_projects')
        else:
            messages.error(request, 'Person as technology is not valid')
    return render(request, 'create_project.html', {"form": form})


def get_projects(request):
    data = request.POST
    if data:
        key = data.get('filter')
        projects = {} if key is None else Project.objects.filter(title__contains=key)
        messages.success(request, "Projects returned successfully")
    else:
        projects = Project.objects.all().order_by('-date_created')
    return render(request, 'project_list.html', {"projects": projects})


def filter_project(request):
    data = request.POST
    key = data.get('filter')
    projects = {} if key is None else Project.objects.filter(title__contains=key)
    return render(request, 'filtered_project.html', {"projects": projects})


def delete_project(request, id):
    if Project.objects.filter(id=id).exists():
        Project.objects.get(id=id).delete()
    return redirect('view_all_projects')


def retrieve_project(request, id):
    if Project.objects.filter(id=id).exists():
        projects = Project.objects.get(id=id)
    else:
        projects = {}
    return render(request, 'project_detail.html', {'projects': projects})


def update_project(request, the_id):
    projects = Project.objects.get(id=the_id)
    form = ProjectForm(instance=projects)
    data = request.POST
    print(data)
    if request.method == "POST":
        form = ProjectForm(instance=projects, data=data)
        if form.is_valid() and data.get('technology') != "person":
            form.save()
            return redirect('project_details', the_id)
        else:
            print("This object will not save")
            print("The technology should not be person")
            print(form.errors)
    return render(request, 'update_project.html', {'projects': projects, 'form': form})
