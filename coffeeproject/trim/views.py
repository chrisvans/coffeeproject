from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import URLValidator
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.template import Context, loader
from trim.models import Trimurl

def home_view(request):
    return HttpResponseRedirect('/trim/')

def trim(request):
    error_message = None
    success_message = None
    information_message = None
    if request.method == 'POST':
        url = request.POST['url']
        validate = URLValidator()

        try:
            validate(url)
            print url

            url = url.replace('https://', '')
            url = url.replace('http://', '')

            check_for_url = Trimurl.objects.filter(url=url)

            if check_for_url.exists():
                success_message = 'URL ' + url + ' Successfully trimmed to ' + 'abcdef' + '!'
                information_message = 'Access your url at coffeeproject.herokuapp.com/trim/' + 'adcdef/'


        except ValidationError, err_msg:
            error_message = 'That is not a valid URL.'

    return render(request, 'index.html', {
                                        'error_message' : error_message,
                                        'success_message' : success_message,
                                        'information_message' : information_message })

def trimmed_url(request, trimmed_url=None):
    url = None
    trimurl = None

    if trimmed_url:

        try:
            trimurl = Trimurl.objects.get(trimmed_url=trimmed_url)
            url = trimurl.url

        except (KeyError,Trimurl.DoesNotExist):
            error_message = "URL wasn't found."

    if url:
        return HttpResponseRedirect('http://'+url)
    else:
        return render(request, 'index.html', {'error_message': error_message})



