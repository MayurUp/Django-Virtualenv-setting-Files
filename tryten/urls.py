from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from profiles import views as profiles_views
from contact import views as contact_views
from checkout import views as checkout_views
from posts import views as posts_views
#from posts import views as post_create_views

urlpatterns = [
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^admin/', admin.site.urls),
    url(r'^profiles/', profiles_views.home, name='home'),
    url(r'^about/', profiles_views.about, name='about'),
    url(r'^profile/', profiles_views.userProfile, name='profile'),
    #url(r'^profile/(?P<username>[\w.@+-]+)/$', profiles_views, name='profile'),
    url(r'^checkout/', checkout_views.checkout, name='checkout'),
    url(r'^contact/', contact_views.contact, name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^post/', post_views.Post, name='posts'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)