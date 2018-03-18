from django.template.loader import get_template
from django.http import HttpResponse, Http404
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render({'current_date': now})
    return HttpResponse(html)