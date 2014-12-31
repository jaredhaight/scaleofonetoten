from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


def register_view(request):
    return render_to_response('register.html', context_instance=RequestContext(request))


def login_view(request):
    logout(request)
    username = password = ''
    try:
        next_value = request.GET["next"]
    except:
        next_value = None

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            next_value = request.POST['next_value']
        except:
            next_value = None

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if next_value:
                    return HttpResponseRedirect(next_value)
                return HttpResponseRedirect(reverse('account.views.profile_view'))
    d = dict(next_value=next_value)
    return render_to_response('login.html', d, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")