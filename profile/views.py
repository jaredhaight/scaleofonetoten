from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from profile.models import Notification
from profile.forms import HayUserForm, NotificationForm
from django.utils import timezone

@login_required()
def home(request):
    user = request.user
    notification = Notification.objects.filter(user=user).first()
    user_form = HayUserForm(instance=user, prefix="u_")
    notification_form = NotificationForm(instance=notification, prefix="n_")
    result = None
    if request.POST:
        user_form = HayUserForm(request.POST, prefix="u_", instance=user)
        notification_form = NotificationForm(request.POST, prefix="n_", instance=notification)
        if user_form.is_valid() and notification_form.is_valid():
            user_form.save()
            notification_form.user = user.id
            notification_form.save()
            result = "Form Saved!"
    d = dict(user=user, user_form=user_form, notification_form=notification_form, result=result)
    return render_to_response('profile_home.html', d, context_instance=RequestContext(request))
