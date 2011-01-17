from django.conf.urls.defaults import *
from views import *


urlpatterns = patterns('',
   url(r'^$', home, name="home"),
   url(r'^pdf/$', get_pdf, name="get_pdf"),
)

