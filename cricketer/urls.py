from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('viewall', views.viewall,name='viewall'),
    path('', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('home', views.home,name='home'),
    path('viewteam', views.viewteam,name='viewteam'),
    path('verify', views.verify,name='verify'),
    path('bid/<str:name>/', views.bid,name='bid'),
    path('<str:name>/',views.profile,name="profile"),
    path('sendmail', views.sendmail,name='sendmail'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)