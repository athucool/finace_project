"""finance URL Configuration

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
from django.conf.urls import url


from django.contrib import admin
from django.urls import path,include
from Account.views import Register,user_login,index,user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',Register,name="register"),
    path('',index,name="index"),
    path('login/',user_login,name="login"),
    path('logout/',user_logout,name="logout"),
    url(r'^report_builder/', include('report_builder.urls')),
    path("finance/",include("Report.urls",namespace="report")),
    path("payment/",include("Finance_Manager.urls",namespace="financeManager")),


]

