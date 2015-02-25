from django.conf.urls import patterns, include, url
from app.views import archive

urlpatterns = patterns('',
    url(r'^$',archive),
)