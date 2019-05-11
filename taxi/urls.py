from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^getgroups/(?P<from_pl>[^$]+)_(?P<to_pl>[^$]+)_(?P<time>[^$]+)/$', views.getgroups),
    url(r'^join/(?P<man_id>[^$]+)_(?P<group_id>[0-9]+)/$', views.join),
    url(r'^leavegroup/(?P<man_id>[^$]+)/$', views.leavegroup),
    url(r'^releasegroup/(?P<group_id>[0-9]+)/$', views.releasegroup),
    url(r'^getgroupstate/(?P<group_id>[0-9]+)/$', views.getgroupstate),
    url(r'^creategroup/(?P<man_id>[^$]+)/$', views.creategroup)
]