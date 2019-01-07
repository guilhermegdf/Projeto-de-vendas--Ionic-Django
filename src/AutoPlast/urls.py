"""AutoPlast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from dashboard.views import *
from authentication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('index/', index),
    path('postsign/', postsign),
    path('logout/', logout, name='log'),
    path('all_users/', users_list),
    path('new_user/', create_user),
    path('pendent_user/', pedent_user),
    path('postsignup/', postsignup, name='postsignup'),
    path('user_info/<id>', userinfo, name='infouser'),
    path('postputuser/<id>', postputuser),
    path('all_order/', order_list),
    path('user_info/<id>', orderinfo, name='inforder'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
