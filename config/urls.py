"""
URL configuration for dost_index project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.decorators.http import require_GET
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings


@require_GET
def custom_logout(request):
    logout(request)
    return redirect('/admin')


urlpatterns = [
    path('admin/logout/', custom_logout, name='logout'),
    path('admin/', admin.site.urls),
    path('', admin.site.urls),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
