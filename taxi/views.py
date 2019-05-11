from django.shortcuts import render
from django.http import JsonResponse
from . import calculations

def getgroups(request, from_pl, to_pl, time):
    #return JsonResponse({"answer": "get all groups from " + from_pl +
    #                    " to " + to_pl + " in " + time})
    return calculations.getGroupsJson(request, from_pl, to_pl, time)


def join (request, man_id, group_id):
    #return JsonResponse({"answer" : "join user with id " + man_id +
    #                    " to group with id " + group_id})
    calculations.joinToGroup(request, man_id, group_id)

def leavegroup(request, man_id):
    #return JsonResponse({"answer": "user with id " + man_id +
    #                     " leaves his group"})
    return calculations.leaveGroup(request, man_id)


def releasegroup(request, group_id):
    #return JsonResponse({"answer": "group with id " + group_id +
    #                    " is launched"})
    return calculations.deleteGroup(request, group_id)

def getgroupstate(request, group_id):
    #return JsonResponse({"answer": "state of the group with id " + group_id})
    return calculations.getGroupStateJson(request, group_id)


def creategroup(request, man_id, from_pl, to_pl, time):
    #return JsonResponse({"answer" : "creating group with head user with id " + man_id})
    return calculations.createGroup(request, man_id, from_pl, to_pl, time)