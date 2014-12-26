from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render_to_response('home.html')


def register(request):
    return render_to_response('register.html')


def login_view(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    return render_to_response('login.html', context_instance=RequestContext(request))