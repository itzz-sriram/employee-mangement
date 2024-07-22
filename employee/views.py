from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def create(request):
    
    if request.method == 'POST':
        employee_Form = employeeForm(request.POST)
        if employee_Form.is_valid():
            employee_Form.save()

    return render(request,"pages/index.html", {'employee_Form' : employeeForm()})

def read(request):
    context = {
        'all_details' : usr_profile.objects.all()
    }
    return render(request, 'pages/show.html',context)

def delete(request,id):
    selected_usr = usr_profile.objects.get(id = id)
    selected_usr.delete()
    return redirect('/read/')




def update(request, id):

    selected_usr = usr_profile.objects.get(id=id)

    
    if request.method == "POST":
        employee_Form = employeeForm(request.POST, instance=selected_usr)
        if employee_Form.is_valid():
            employee_Form.save()

            return redirect('/read/')
    
        
    return render(request,'pages/index.html',{'employee_Form' : employeeForm(instance=selected_usr)})
