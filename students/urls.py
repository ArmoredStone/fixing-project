from django.conf.urls import url
from students.views import students_controller, groups_controller

urlpatterns = [
    #Students Urls
    url(r'', students_controller.students_list, name='home'),
    url(r'students_add/', students_controller.students_add, name='students_add'),
    url(r'(?P<sid>\d+)/edit/', students_controller.students_edit, name='students_edit'),
    url(r'(?P<sid>\d+)/delete/', students_controller.students_delete, name='students_delete'),

    # Groups urls
    url(r'groups/', groups_controller.groups_list, name='groups'),
    url(r'groups/add/', groups_controller.groups_add, name='groups_add'),
    url(r'groups/(?P<gid>\d+)/edit/', groups_controller.groups_edit, name='groups_edit'),
    url(r'groups/(?P<gid>\d+)/delete/', groups_controller.groups_delete, name='groups_delete'),
]
