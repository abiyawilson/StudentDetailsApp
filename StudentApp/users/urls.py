from django.urls import path

from users import views

urlpatterns = [
    path('user/create/', views.UserAccountView.as_view()),
    path('users/list/', views.UsersListView.as_view()),
    path('user/auth/', views.CustomAuthToken.as_view())
]