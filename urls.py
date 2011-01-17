from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to


urlpatterns = patterns('',
    (r'^$', redirect_to, {'url': '/latex/'}),
    (r'^latex/', include('latex.urls',
                  namespace="latex",
                  app_name="latex")),
)
