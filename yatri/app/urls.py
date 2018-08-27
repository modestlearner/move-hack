from django.conf.urls import url,include
from django.urls import path

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url


urlpatterns = [
    # url(r'^$', views.HomePageView.as_view()),
    # url(r'^links/$' , views.LinksPageView.as_view()),
    # url(r'^journeys/$', views.journeys),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^todo/$', views.TodoList.as_view(),name='todo'),
    url(r'^vehicle/$', views.Vehiclelist.as_view(),name='vehicle'),
    url(r'^aadhaar/$', views.Aadhaarlist.as_view()),
    #url(r'^api-token-auth/', views.obtain_auth_token)



]
urlpatterns = format_suffix_patterns(urlpatterns)