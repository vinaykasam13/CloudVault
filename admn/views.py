from django.shortcuts import render,HttpResponse
from user.models import CloudUsersModel

from django.contrib import messages


def adminlogin(request):
    return render(request,'adminlogin.html')

def adminlogincheck(request):
    if request.method == "POST":
        usid = request.POST.get('name')
        pswd = request.POST.get('password')
        print("User ID is = ", usid)
        if usid == 'admin' and pswd == 'admin':
            request.session['role'] = 'admin'
            return render(request, 'admin/adminhome.html')
        else:
            messages.success(request, 'Invalid Login Details')
    return render(request,'adminlogin.html')

def adminactivateusers(request):
    dict = CloudUsersModel.objects.all()
    return render(request,'admin/activateuser.html',{'objects':dict})

def activatewaitedusers(request,id):
    if request.method == 'GET':
        #uid = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id,status)
        CloudUsersModel.objects.filter(id=id).update(status=status)
    dict = CloudUsersModel.objects.all()
    return render(request, 'admin/activateuser.html', {'objects': dict})
