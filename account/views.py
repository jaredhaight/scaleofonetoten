from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from account.models import Notification, Result
from account.forms import OTTUserForm, NotificationForm


@login_required()
def profile_view(request):
    user = request.user
    notification = Notification.objects.filter(user=user).first()
    user_form = OTTUserForm(instance=user, prefix="u_")
    #TODO - If a notification doesn't exist already, this bombs out. I should fix that.
    notification_form = NotificationForm(instance=notification, prefix="n_")
    result = None
    if request.POST:
        user_form = OTTUserForm(request.POST, prefix="u_", instance=user)
        notification_form = NotificationForm(request.POST, prefix="n_", instance=notification)
        if user_form.is_valid() and notification_form.is_valid():
            user_form.save()
            notification_form.user = user.id
            notification_form.save()
            result = "Form Saved!"
    d = dict(user=user, user_form=user_form, notification_form=notification_form, result=result)
    return render_to_response('profile_home.html', d, context_instance=RequestContext(request))


@login_required
def dashboard_view(request):
    user = request.user
    results = Result.objects.filter(user=user)
    date_list = list()
    result_list = list()
    for r in results:
        result_list.append(r.value)
        date_list.append(r.time.strftime("%x"))
    d = dict(date_list=date_list, result_list=result_list, results=results)
    return render_to_response('dashboard_home.html', d,
                              context_instance=RequestContext(request))


