from django.urls import path
from .views import RegistrationApiView, GetAllUser, LoginApiView, LogoutApiView

urlpatterns = [
    path('registration/', RegistrationApiView.as_view()),
    path('all/users/', GetAllUser.as_view()),
    path('login/', LoginApiView.as_view()),
    path('logout/', LogoutApiView.as_view())
]