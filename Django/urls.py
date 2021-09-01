from django.conf.urls import include, url
from django.conf import settings
from django.views.static import serve
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
	url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
	url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('App1.urls')),   
]