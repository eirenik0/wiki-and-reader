from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
                      url(r'^chronology/$', views.ChronologyView.as_view(), name="chronology"),

                       url(r'^contact-us/$', views.ContactView.as_view(), name="contact_us"),
                       url(r'^thanks/$', views.ThanksView.as_view(), name="thanks"),
)
