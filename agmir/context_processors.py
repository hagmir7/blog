from django.contrib.auth.models import User
from scraping.models import Contact, Link, Settings
from django.conf import settings as setting


def context_data(request):
    messages = Contact.objects.filter(readed=None)
    footer = Link.objects.filter(footer=True) 
    header = Link.objects.filter(header=True)
    settings = Settings.objects.last() 

    return {
        'messages': messages,
        'footer' : footer,
        'header' : header,
        'settings' : settings,
        'cpanel' : setting.CPANEL
        }
    