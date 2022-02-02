from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth import login,authenticate, logout,update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponseRedirect

from learning.models import signup
from .forms import hubsign_up,Edituserprofileform,EditAdminprofileform,user_login
from django.contrib.auth import login,authenticate, logout,update_session_auth_hash
from django.contrib import messages

# Create your views here.



#website page
def homepage(request):
    return render(request,'blog/home.html')





#about page
def abou(request):
    return render(request,'blog/about.html')







# contact page

def cont(request):
    return render(request,'blog/contact.html')






def showsignin(request):
    if request.method=='POST':
         sm=hubsign_up(request.POST)
         if sm.is_valid():
            messages.success(request,'ACCOUNT CREATE SUCESSFULLY')
            sm.save()
            
    else:
        sm=hubsign_up()
    return render(request,'blog/signup.html',{'forms':sm})






#login
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
              form=user_login(request=request,data=request.POST)
              if form.is_valid():
                  uname=form.cleaned_data['username']
                  upass=form.cleaned_data['password']
                  user= authenticate(username=uname,password=upass)
                  if user is not None:
                      login(request,user)
                      messages.success(request,'Logged in Sucessfully!!')
                      return HttpResponseRedirect(request,'blog/python-firststep.html')

        else:
            form=user_login()
        
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')



#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')




#  Profile

def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            if request.user.is_superuser==True:
                fm=EditAdminprofileform(instance=request.user)
            else:
                fm=Edituserprofileform(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'Profile Updated !!!')
                fm.save()
        else:
            if request.user.is_superuser==True:
                fm=EditAdminprofileform(instance=request.user)
            else:   
                fm=Edituserprofileform(instance=request.user)
        return render(request,'blog/profile.html', {'name':request.user.username,'form':fm})
    else:
        return HttpResponseRedirect('/login/')






#user change password

def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password change sucessfully...')
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'blog/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')



# def python_first(request):
#     if not request.user.is_authenticated:
#         if request.method =="POST" :
#             return render(request,'blog/python-firststep.html')

#     else:
#         return HttpResponseRedirect('/login/')
