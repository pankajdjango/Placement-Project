from django.shortcuts import render, redirect
from .forms import StudentForm,CompanyForm
from .models import Students,Companies

# Create your views here.
def index(reqeust):
    return render(reqeust,"index.html")


def register_student(request):
    context = dict()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Student Register Successfully."
        else:
            msg = "Something went wrong!"
        context.update({"res":msg})

    context.update({
        'form': StudentForm(),
        "students":Students.objects.all()
    })
    return render(request,"add_student.html", context)


def register_company(request):
    context = dict()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Company Register Successfully."
        else:
            msg = "Something went wrong!"
        context.update({"res":msg})

    context.update({
        'form': CompanyForm(),
        "companies":Companies.objects.all()
    })
    return render(request, 'company_registration.html',context)
