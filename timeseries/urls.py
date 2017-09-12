"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'acoustic$', views.acoustic, name = 'acoustic'),
    url(r'acoustic/motivation$', views.acoustic_intro, name = 'acoustic_motivation'),
    # url(r'acoustic/techniques$', views.acoustic_tech, name = 'acoustic_techniques'),
    # url(r'acoustic/outcome$', views.acoustic_resl, name = 'acoustic_outcome'),
    url(r'supersonic$', views.supersonic, name = 'supersonic'),
    url(r'supersonic/motivation$', views.supersonic_intro, name = 'supersonic_motivation'),
]
