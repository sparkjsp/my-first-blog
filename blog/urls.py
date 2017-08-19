from django.conf.urls import url
from . import views
#from django.conf.urls.static import static

urlpatterns = [
    #url(r'^$',views.post_list, name='post_list'),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$',views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    
    url(r'^$',views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$',views.single, name='single'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^about/$',views.about, name='about'),
    
]


