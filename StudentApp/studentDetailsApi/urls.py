from django.urls import path

from studentDetailsApi import views

urlpatterns = [
    path('studentsDetails/list/', views.StudentsRecordsList.as_view()),
    path('studentsDetails/create/', views.StudentRecordCreate.as_view()),
    path('studentDetails/show/<int:pk>/', views.StudentRecord.as_view),
    path('studentDetails/update/<int:pk>/', views.StudentRecordUpdate.as_view),
    path('studentDetails/delete/<int:pk>/', views.StudentRecordDelete.as_view),
]
