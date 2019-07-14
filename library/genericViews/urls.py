from django.conf.urls import url
from . import views
app_name = 'genericViews'
urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^bookenter/$', views.makeentry, name='bookenter'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^allentries/$', views.IndexView.as_view(), name='index'),

]
