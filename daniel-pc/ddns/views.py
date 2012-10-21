import sys
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from models import IP
import datetime


def index(request):
    template = loader.get_template('index.html')
    context = Context({
        'var': 0,
    })
    return HttpResponse(template.render(context))


def addip(request):
    ip_txt = ""
    if request.method == 'GET':
        ip_txt = request.GET.get('ip')
    elif request.method == 'POST':
        ip_txt = request.POST.get('ip')
    try:
        if ip_txt != "" and ip_txt != None:
            ip = IP(IP=ip_txt, date=datetime.datetime.now())
            ip.save()
            ans = "IP %s added." % ip_txt
            return HttpResponse(ans)
        else:
            return HttpResponse("No IP.")
    except:
        return HttpResponse("Couldnt add %s to db." % ip_txt)


def redirect(request):
    ip = IP.objects.latest('date')
    return HttpResponseRedirect(str("http://%s" % ip.IP))


def createuser(request):
    if authenticate(username='daniel', password='pass') is not None:
        return HttpResponse("User already created ;)")
    try:
        user = User.objects.create_user('daniel', 'daniel@ctrl68.com', 'pass')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return HttpResponse("User created! :)")
    except:
        print sys.exc_info()[0]
        return HttpResponse("Couldnt\' create user :(")
