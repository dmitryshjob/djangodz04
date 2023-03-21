from django.views.generic import ListView
from django.shortcuts import render

from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students_object = Student.objects.all().order_by('group',)
    context = {'object_list': students_object}


    return render(request, template, context)




