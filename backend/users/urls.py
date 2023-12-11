from django.urls import path

from . import views

urlpatterns = [
    path(
        "login/",
        views.TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("", views.getUsers, name="users-list"),
    path("profile/", views.getUserProfile, name="user-profile"),
    path("register/", views.registerUser, name="user-register")
]
