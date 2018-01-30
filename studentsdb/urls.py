from django.urls import  path, include
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    # Students And Groups urls
    path(r'students/',include('students.urls')),
    path(r'', RedirectView.as_view(url = r'/students/')),
    #Admin urls
    path(r'admin/', admin.site.urls),
]
