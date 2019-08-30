"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers

from rest_framework_swagger.views import get_swagger_view

from randomwalk import views

# Routers
# Can register multiple routers

router = routers.DefaultRouter()
router.register(r'randomwalk', views.SampleDataView, 'randomwalk')
router.register(r'blackscholes', views.BlackScholesView, 'blackscholes')
router.register(r'brownianmotion', views.BrownianMotionView, 'brownianmotion')
# Swagger Docs

schema_view = get_swagger_view(title='Random Walk API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api2/', views.StaticView.as_view()),
    path('axios_test/', views.AxiosView.as_view()),
    path('swagger/', schema_view)
]
