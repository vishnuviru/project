from django.conf.urls import include, url
from django.contrib import admin




from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'Tollplaza_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^',include('Tollplaza_api_app.urls')),
    url(r'^static/', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
]
if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
