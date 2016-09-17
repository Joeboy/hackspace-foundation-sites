from django.http import HttpResponse
from django.contrib.auth.views import redirect_to_login

import requests

from main.models import User


def get_user(request):
    try:
        r = requests.get('http://localhost/session.php',
                         cookies=request.COOKIES)
        d = r.json()
        user_id = int(d.get('user_id'))
        user = User.objects.get(pk=user_id)
    except:
        user = None
    return user


def php_login_required(f):
    def _inner(request, *args, **kwargs):
        if 'PHPSESSID' not in request.COOKIES:
            return redirect_to_login(request.path,
                                     redirect_field_name='forward')
        user = get_user(request)
        if user is None:
            return redirect_to_login(request.path,
                                     redirect_field_name='forward')

        request.user = user
        return f(request, *args, **kwargs)

    return _inner


def auth_test(request):
    user = get_user(request)
    return HttpResponse("User=" + (user.full_name if user else "Anon"))


@php_login_required
def auth_required_test(request):
    return HttpResponse("Oy " + request.user.full_name + ". You are probably mostly logged in probably.")
