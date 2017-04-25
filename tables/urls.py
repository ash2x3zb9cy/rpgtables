from django.conf.urls import url
from . import views
from django.views import generic
urlpatterns = [
	url(r'^$', views.Index.as_view(template_name='tables/index.html'), name='table_index'),
	url(r'^(?P<pk>[0-9]+)/$', views.Detail.as_view(), name='table_detail'),
	url(r'^(?P<pk>[0-9]+)/delete/$', views.Delete.as_view(), name='table_delete'),
	url(r'^(?P<pk>[0-9]+)/update/$', views.Update.as_view(), name='table_update'),
	url(r'^(?P<pk>[0-9]+)/save/$', views.save, name='table_save'),
	url(r'^create/$', views.Create.as_view(), name='table_create'),
]
