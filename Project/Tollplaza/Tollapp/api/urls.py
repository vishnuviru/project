from django.conf.urls import include, url,patterns
from django.contrib import admin
from Tollapp.views import *



from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from .views import (
    MainListAPIView
    )



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tollplaza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),


    url(r'^$', MainListAPIView.as_view(),name='list'),
    url(r'^MainListAPIView/',MainListAPIView),
    

    


)
if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
