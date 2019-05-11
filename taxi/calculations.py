from django.http import JsonResponse
from datetime import datetime
from django.core import serializers
from .models import TaxiGroup, TaxiPlaceholder

def getGroupsJson(request, from_pl, to_pl, time):
    this_time = datetime.strptime(time, '%H:%M %d.%m.%Y')
    return serializers.serialize('json', TaxiGroup.objects.filter(from_place=from_pl, to_place=to_pl, leave_time=this_time))


def createGroup(request, man_id):
