"""
Definition of urls for mySecondWebProject.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^landingpage/(?P<service_id>\w+)/$', 'mooncakeTestEnvironment.views.landingPage', name='landingPage'),
    url(r'^landingpage/$', 'mooncakeTestEnvironment.views.index', name='landingPageIndex'),
    url(r'^xmlpagegenerator/(?P<service_id>\w+)/$', 'mooncakeTestEnvironment.views.xmlpagegenerator', name='xmlpagegenerator'),
    url(r'newrecentupdate/(?P<counter>[0-9]+)/$', 'mooncakeTestEnvironment.views.newRecentUpdate', name='newRecentUpdate'),
    url(r'^editTutorialSelectList/(?P<service_id>\w+)/$', 'mooncakeTestEnvironment.views.editTutorialSelectList', name='editTutorialSelectList'),
    url(r'newTutorialOption/(?P<counter>[0-9]+)/$', 'mooncakeTestEnvironment.views.newTutorialOption', name='newTutorialOption'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
