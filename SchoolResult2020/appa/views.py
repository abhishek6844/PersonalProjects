from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
from django.db.models import Sum, Avg, Max, Min
from .forms import StudentsForm






# Create your views here.

def Jupiter(request):
    mainList = []
    for i in range(1,6):
        x = Students.objects.all().filter(standard=i)
        s = Students.objects.filter(standard=i).aggregate(Sum('marks'))
        z = Students.objects.all().filter(standard=i).aggregate(Max('marks'))
        t_list = Students.objects.all().filter(standard=i, marks=z['marks__max'])
        e = [x,s,z,i,t_list]
        mainList.append(e)

    return render(request, 'first.html',context= {'mainList':mainList})

def StudentForm(request):
    if request.method == 'POST':
        Student_Form = StudentsForm(data=request.POST)
        if Student_Form.is_valid():
            student = Student_Form.save()
            student.save()
            Student_Form = StudentsForm()
        else:
            print("encuraptted information")
    else:
        Student_Form = StudentsForm()
    return render(request,'studentsform.html',context={'StudentsForm':Student_Form})
