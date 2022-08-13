from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy
from .models import Members
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers


def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({}, request))


def json(request):
    mymembers = Members.objects.all()
    tmpJson = serializers.serialize("json", mymembers)
    return JsonResponse(tmpJson, safe=False)


def addrecord(request):
    x = request.POST["first"]
    y = request.POST["last"]
    members = Members(firstname=x, lastname=y)
    members.save()
    return HttpResponseRedirect(reverse("index"))
