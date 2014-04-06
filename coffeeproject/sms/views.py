# Django
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Third Party
import twilio.twiml
 
@csrf_exempt
def receive_message(request):

    if request.POST.get('Body'):
        if 'no' in request.POST.get('Body'):
            response = twilio.twiml.Response()
            response.message("The door will not be opened.")
        elif 'yes' in request.POST.get('Body'):
            response = twilio.twiml.Response()
            response.message("The door will be opened.")
        else:
            response = twilio.twiml.Response()
            response.message("""
                Sorry, you need to reply with a yes or no.
                """)

    return HttpResponse(response, content_type='text/xml')