"""mud_pi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path

admin.site.site_header = 'Mud-Py'                    # default: "Django Administration"
admin.site.index_title = 'Mud-Py administration'                 # default: "Site administration"
admin.site.site_title = 'Mud-Py administration' # default: "Django site admin"

urlpatterns = [
    path('controlnode/', include('controlnode.urls')),
    path('zone/', include('zone.urls')),
    path('admin/', admin.site.urls),
]