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
    url(r'algorithm$', views.algorithm, name = 'algorithm'),
    url(r'algorithm/motivation$', views.algo_intro, name = 'algo_motivation'),
    url(r'algorithm/techniques$', views.algo_tech, name = 'algo_techniques'),
    url(r'algorithm/outcome$', views.algo_resl, name = 'algo_outcome'),
    url(r'visualize$', views.visualize, name = 'visualize'),
    url(r'visualize/motivation$', views.vis_intro, name = 'vis_motivation'),
    url(r'visualize/techniques$', views.vis_tech, name = 'vis_techniques'),
    url(r'visualize/outcome$', views.vis_resl, name = 'vis_outcome'),
]