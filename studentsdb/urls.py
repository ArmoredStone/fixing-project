from django.urls import  path, include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    # Students And Groups urls
    path(r'students/',include('students.urls')),
    #Admin urls
    url(r'admin/', admin.site.urls),
]
