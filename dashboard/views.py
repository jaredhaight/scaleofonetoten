from django.shortcuts import render_to_response, HttpResponse
from django.contrib.auth.decorators import login_required
from dashboard.models import Result


@login_required
def home(request):
    user = request.user
    results = Result.objects.filter(user=user)
    date_list = list()
    result_list = list()
    for r in results:
        result_list.append(r.value)
        date_list.append(r.time.strftime("%x"))
    return render_to_response('dashboard_home.html', dict(date_list=date_list, result_list=result_list))

