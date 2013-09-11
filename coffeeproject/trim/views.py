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
import random, string

def home_view(request):
    # '/' View
    return HttpResponseRedirect('/trim/')

def trim(request):
    # '/trim' View for url input and trimming
    error_message = None
    success_message = None
    information_message = None

    if request.method == 'POST':
        url = request.POST['url']
        validate = URLValidator()

        try:
            
            # Add http for proper validation check
            if url[0:4] != 'http':
                url = 'http://' + url

            validate(url)
            
            # Remove http / s for generic url storage
            url = url.replace('https://', '')
            url = url.replace('http://', '')

            check_for_url = Trimurl.objects.filter(url=url)
            
            # If the url already exists, don't create a new entry, refer to the old one instead
            if check_for_url.exists():
                old_trimurl = check_for_url[0]
                success_message = 'URL ' + url + ' Successfully trimmed to ' + old_trimurl.trimmed_url + '!'
                information_message = 'Access your url at www.cutlink.us/trim/' + old_trimurl.trimmed_url + '/'

            else:
                new_trimurl = Trimurl()
                check_for_existing_trimmed_url = True
                
                # Assure that a new unique trimmed url is generated
                while check_for_existing_trimmed_url:
                    trimmed_url = ''.join(random.choice(string.ascii_lowercase) for x in range(6))
                    check_for_trimmed_url = Trimurl.objects.filter(trimmed_url=trimmed_url)
                    check_for_existing_trimmed_url = check_for_trimmed_url.exists()

                new_trimurl.trimmed_url = trimmed_url
                new_trimurl.url = url
                new_trimurl.save()
                success_message = 'URL ' + url + ' Successfully trimmed to ' + trimmed_url + '!'
                information_message = 'Access your url at www.cutlink.us/trim/' + trimmed_url + '/'


        except ValidationError, err_msg:
            error_message = 'That is not a valid URL.'

    return render(request, 'index.html', {
                                        'error_message' : error_message,
                                        'success_message' : success_message,
                                        'information_message' : information_message })

def trimmed_url(request, trimmed_url=None):
    # /trim/<trimmed_url> View for redirection to proper page
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



