from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #Auth URLs
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/' }, name='logout'),
    url(r'^account/password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^account/password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^account/password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^account/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^account/reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^account/reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    #Core URLs
    url(r'^$', TemplateView.as_view(template_name='core/index.html'), name='index'),
    url(r'^account/$', 'core.views.account', name='account'),
    url(r'^register/$', 'core.views.register', name='register'),
    url(r'^register/done$', 'core.views.register_done', name='register_done'),

)

urlpatterns += staticfiles_urlpatterns()