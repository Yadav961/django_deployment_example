from django.conf.urls import url
from basic_app import views

#TEMPLATE TAGGING app_name IS GLOBAL VARIABLE LOOK UNDER BASIC APP FOR THE MATCHING URLS.
app_name = 'basic_app'

#CREATING ULR PATTERS LIST

urlpatterns = [

    url(r'^relative/$', views.relative, name = 'relative'),
    url(r'^other/$', views.other, name = 'other'),
    url(r'^clickbit/$', views.clickbit, name = 'clickbit')

]
