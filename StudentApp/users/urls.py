from django.urls import path
from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
)

from users import views

urlpatterns = [
    path('user/create/', views.UserAccountView.as_view()),
    path('users/list/', views.UsersListView.as_view()),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]