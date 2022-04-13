from django.shortcuts import render


def small_project(request):
    return render(request, 'small_project.html', {})
