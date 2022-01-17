from django.urls import path

from studentDetailsApi import views

urlpatterns = [
    path('studentsDetails/list/', views.students_list),
    path('studentsDetails/create/', views.student_create),
    path('studentDetails/show/<int:pk>/', views.student_detail),
    path('studentDetails/update/<int:pk>/', views.student_detail_update),
    path('studentDetails/delete/<int:pk>/', views.student_detail_delete),
]
