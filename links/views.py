from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import random
from .models import *


# Create your views here.
def index(request):
    goods = []
    bads = []
    i = 0
    link_objects = [x for x in Link.objects.all()]
    random.shuffle(link_objects)
    for l in link_objects:
        if l not in goods:
            if l.risk > 0:
                goods.append(l)
        i += 1
        if i == 7:
            break
    for l in goods:
        for b in link_objects:
            if b not in bads:
                if b.risk == l.risk * -1:
                    bads.append(b)
    zipped = [x for x in zip(goods, bads)]
    context = {
        'links': zipped,
    }
    return render(request, 'links/index.html', context)


def post(request):
    display = request.POST['display_text']
    address = request.POST['address']
    risk = request.POST['risk']

    return HttpResponseRedirect(reverse('links:index'))