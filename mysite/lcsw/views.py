from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from lcsw.models import Excuse
import random
def home(request):
#    excuses = [
#        "It was working in my head",
#        "I thought I fixed that",
#        "Actually, that is a feature",
#        "It works on my machine",
#    ]
    excuse = random.choice(Excuse.objects.all())
    return render(request, "index.html", {'excuse': excuse})
