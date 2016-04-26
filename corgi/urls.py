from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'corgi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^postreply/',include('postreply.urls')),
    
)


if settings.DEBUG:

	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$','django.views.static.serve',
			{'document_root':settings.MEDIA_ROOT}),
		)