"""decide URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from decide import views

   
schema_view = get_swagger_view(title='Decide API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/', schema_view),
    path('gateway/', include('gateway.urls')),
    path('helpvoiceassistant/', views.HelpVoiceAssistantView.as_view(), name="helpVoiceAssistant"),
    path('modifyProfileData/', views.ModifyProfileDateView.as_view(), name="modifyProfileData"),
    path('sign-in/', views.SignInView.as_view(), name="signIn"),
    path('login/', views.login, name="indexlogin"),
    path('logout/', views.logout, name="indexlogout"),
    path('', views.IndexView.as_view(), name="index")
]

for module in settings.MODULES:
    urlpatterns += [
        path('{}/'.format(module), include('{}.urls'.format(module)))
    ]