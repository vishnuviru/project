from django.conf.urls import include, url,patterns
from django.contrib import admin
from Tollapp.views import *



from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tollplaza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', mainpage),
    url(r'^display_homepage/',display_homepage),
    url(r'^get_details/',get_details),
    url(r'^edit_property/',edit_property),
    url(r'^save_edit_property/',save_edit_property),
    url(r'^sign_up/',sign_up),
    url(r'^signup_data/',signup_data),
    url(r'^clear/',clear_page),
    url(r'^search/',search),
    url(r'^search_reports/',search_reports),
    url(r'^report/',report),
    url(r'^index/',index),
    url(r'^edit_lanenumber/',edit_lanenumber),
    url(r'^logout/',logout),
    url(r'^reset_pass/',reset_pass),
    url(r'^reset_password/',reset_password),
    url(r'^chart/',chart),
    url(r'^create$', create),
    url(r'^create_cam$', create_cam),
    url(r'^create_user$', create_user),
    url(r'^index/', index),
    url(r'^index_cam/', index_cam),
    url(r'^index_user/', index_user),
    url(r'^edit/(?P<id>\d+)$',edit),
    url(r'^update/(?P<id>\d+)$',update),
    url(r'^delete/(?P<id>\d+)$',destroy),
    url(r'^search_image/$',search_image),
    url(r'^edit_cam/(?P<id>\d+)$',edit_cam),
    url(r'^update_cam/(?P<id>\d+)$',update_cam),
    url(r'^delete_cam/(?P<id>\d+)$',destroy_cam),
    url(r'^monitor/', monitor),
    url(r'^go/',go),
    url(r'^ANPR/',ANPR),
    url(r'^api/Tollapp/',include("Tollapp.api.urls",namespace='Tollapp-api')),
    url(r'^display/', display),
    url(r'^edit_user/(?P<id>\d+)$',edit_user),
    url(r'^update_user/(?P<id>\d+)$',update_user),
    url(r'^delete_user/(?P<id>\d+)$',destroy_user),
    url(r'^revenue/',revenue),
    url(r'^revenue_report/',revenue_report),
    url(r'^officer/',officer),
	 url(r'^update/',Userpage_update),
	
    


)
if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
