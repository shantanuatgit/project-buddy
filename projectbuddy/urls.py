"""projectbuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from developer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('profileEdit',views.profile_edit_form,name='profileEdit'),
    path('filldetails', views.filldetails_view, name='filldetails'),
    path('accounts/', include('accounts.urls')),
    path('<int:pk>', views.profile_view, name='profileview'),
    path('invites/', views.invites_view, name='invitesview'),
    path('invites/<int:pk> <int:id>', views.accept_response_view, name='acceptview'),
    path('invites/<int:pk>', views.inviter_view, name='inviterview'),
    path('response/', views.request_accepted_view, name='response'),
    path('response/<int:pk>', views.profile_view, name='profileview'),
    path('oauth/', include('social_django.urls', namespace='social')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
