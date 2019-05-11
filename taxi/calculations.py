from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.core import serializers
from .models import TaxiGroup, TaxiPlaceholder


#TODO exceptions everywhere

def getGroupsJson(request, from_pl, to_pl, time):
    this_time = datetime.strptime(time, '%H:%M %d.%m.%Y')
    #TODO cycle to check timediff and free places
    return HttpResponse(serializers.serialize('json', TaxiGroup.objects.filter(from_place=from_pl, to_place=to_pl, leave_time=this_time)))
    #return serializers.serialize('json', TaxiGroup.objects.filter(from_place=from_pl, to_place=to_pl, leave_time=this_time))


def createGroup(request, man_id, from_pl, to_pl, time):
    group = TaxiGroup(from_place=from_pl, to_place=to_pl, leave_time=datetime.strptime(time, '%H:%M %d.%m.%Y'))
    group.save()
    if(TaxiPlaceholder.objects.filter(pk=man_id).exists()):
        taxiPlaceholder = TaxiPlaceholder.objects.get(pk=man_id)
    else:
        taxiPlaceholder = TaxiPlaceholder(pk=man_id, sitting_places_amount=1, group_id=group.pk)
        taxiPlaceholder.save()
    return HttpResponse("group created")


def joinToGroup(request, man_id, group_id):
    group = TaxiGroup.objects.get(pk=group_id)
    taxiPlaceholder = TaxiPlaceholder.objects.get_or_create(pk=man_id, sitting_places_amount=1, group_id=group.pk)
    return HttpResponse("joined group")


def deleteGroup(request, group_id):
    gr = TaxiGroup.objects.get(pk=group_id)
    gr.delete()
    return HttpResponse("group deleted")


def leaveGroup(request, man_id):
    user = TaxiPlaceholder.objects.get(pk=man_id)
    user.delete()
    return HttpResponse("user left group")


def getGroupStateJson(request, group_id):
    gr = TaxiGroup.objects.get(pk=group_id)
    return JsonResponse(
        {"group": str(serializers.serialize('json',[gr])),
         "placeholders": serializers.serialize('json', gr.taxiplaceholder_set.all())})