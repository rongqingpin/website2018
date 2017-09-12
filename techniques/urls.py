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
    url(r'^algorithm$', views.algorithm, name = 'algorithm'),
    url(r'^frequency$', views.frequency, name = 'frequency'),
    url(r'^statistical$', views.statistical, name = 'statistical'),
    url(r'^dimension$', views.dimension, name = 'dimension'),
    url(r'^cluster$', views.cluster, name = 'cluster'),
    url(r'^regression$', views.regression, name = 'regression'),
    url(r'^classify$', views.classify, name = 'classify'),
    url(r'^simulation$', views.simulation, name = 'simulation'),
    url(r'^data$', views.data, name = 'data'),
]
