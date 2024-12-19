"""
URL configuration for Touristmg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from place.views import home
from place.views import aboutus
from place.views import homepage , abtus,table,tour
from place.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("Home",home),
     path("about",aboutus),
      path("Homep",homepage),
      path("abt",abtus),
      path("table1",table),
      path("tour",tour),
      path("travel",travel),path("london",london),
      path('register',location),
      path('show',show),
      path('paris',paris),
      path('nepal',nepal),
       path('mexico',mexico),
         path('malaysia',malaysia),
         path('turkey',turkey),
         path('singapore',singapore),
         path('thailand',thailand),
       path('showall',showall),
       path('demo',demo),
        path('edit/<int:id>',edit),
       

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)