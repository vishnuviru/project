from django.conf.urls import include, url,patterns
from django.contrib import admin
from Tollplaza_api_app.views import *



from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from .views import *
from django.views.decorators.csrf import csrf_exempt



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tollplaza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),


    
    url(r'^$',csrf_exempt(UserLogin.as_view())),
    url(r'^DisplayView/',csrf_exempt(DisplayView.as_view())),
    
)
if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
