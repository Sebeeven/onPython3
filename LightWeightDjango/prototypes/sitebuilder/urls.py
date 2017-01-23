from django.conf.urls import url
from sitebuilder.views import page

urlpatterns = (
    url(r'(?P<slug>[\w./-]+)/$', page, name='page'),
    url(r'^$', page, name='homepage'),
)
