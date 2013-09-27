from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.urlresolvers import reverse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.template import Context, loader
from trim.models import Trimurl, TrimMan
import random, string

def home_view(request):
    # '/' View
    return HttpResponseRedirect('/trim/')

def trim(request, trimmed_url=None):
    # '/trim' View for url input and trimming

    # TrimMan.process_view returns a dictionary in the format:
    # {
    #     'error_message' : error_message,
    #     'url' : url,
    #     'trimmed_url' : trimmed_url,
    # }

    messages = TrimMan.process_view(request, trimmed_url)
    
    message_keys = messages.keys()
    if 'url' in message_keys and 'trimmed_url' in message_keys:
        success_message = 'URL ' + messages['url'] + ' Successfully trimmed to ' + messages['trimmed_url'] + '!'
        information_message = 'Access your url at www.cutlink.us/' + messages['trimmed_url'] + '/'
        messages['success_message'] = success_message
        messages['information_message'] = information_message

    if 'valid_url' in messages.keys() and messages['valid_url']:

        return HttpResponseRedirect('http://'+messages['redirect_url'])

    return render(request, 'index.html', messages)



