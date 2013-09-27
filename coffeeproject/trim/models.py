from django.db import models
from django.core.validators import URLValidator
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied, ValidationError
import random, string

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ExtraModelMethods(models.Model):
    """
    Extra methods applied to classes built around easy information display and utility.
    """

    def attributes(self):
        """
        Prints all attributes of a class ->  Name : Attribute_Value : Attribute_Type
        """
        for field in self._meta.fields:
            attribute_item = getattr(self, field.name)
            print str(field.name) + " : " + str(attribute_item) + " : " + str(type(attribute_item))

    class Meta:
        abstract = True

class Trimurl(TimeStampedModel, ExtraModelMethods):
    # Simple model for storing a url with an associated shortcut key
    trimmed_url = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return unicode("Trim: " + self.trimmed_url + " - URL: " + self.url)

class TrimMan(models.Model):

    @classmethod
    def process_view(self, request, trimmed_url=None):
        # trimmed_url is URI here
        # requires the following line in urls for this view logic
        # url(r'^/path_name(?P<trimmed_url>[a-z]{6})/$', project.views.view_name, name='view_name')

        # the view that process_view is called in must have trimmed_url as an argument

        # process_view expects a view to host a submit field for POST, and deliver status messages 
        # it returns a dictionary with the following information:
        # {
        # 'error_message' : error_message,
        # 'url' : url,
        # 'trimmed_url' : trimmed_url,
        # }

        if trimmed_url:

            url = None
            trimurl = None

            try:
                trimurl = Trimurl.objects.get(trimmed_url=trimmed_url)
                url = trimurl.url

            except (KeyError,Trimurl.DoesNotExist):
                error_message = "URL wasn't found."

            if url:
                return {'valid_url':True, 'redirect_url':url}
            else:
                return {'error_message': error_message}

        error_message = None
        url = None
        trimmed_url = None

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
                    trimmed_url = old_trimurl.trimmed_url

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

            except ValidationError, err_msg:
                error_message = 'That is not a valid URL.'

        return {
                'error_message' : error_message,
                'url' : url,
                'trimmed_url' : trimmed_url,
                }