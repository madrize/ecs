from django.shortcuts import render_to_response
from django.contrib.auth import logout,login,authenticate
from forms import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def mylogin(request,
            logged_in_url="/categories/",
            login_success_url="/categories/",
            template="registration/login.html"):
    """
    login view
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect(logged_in_url)
    
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username,password=password)
        form = AuthenticationForm(request.POST)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(login_success_url)
    else:
        form = AuthenticationForm()
    
    return render_to_response(template,
                              {'form' : form },
                              context_instance=RequestContext(request)) 
            

def register(request,
             register_success_url="/categories/",
             template="registration/register.html",
             logged_in_url="/categories/"):
    """
    Registration view
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect(logged_in_url)
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # form is valid, register the user
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = form.cleaned_data['email']
            )
            return HttpResponseRedirect(register_success_url)
    else:
        form = RegistrationForm()
    
    return render_to_response(template,
                              {'form' : form },
                              context_instance=RequestContext(request)) 


@login_required
def mylogout(request,
             logout_success_url="/categories/"):
    logout(request)
    return HttpResponseRedirect(logout_success_url)

