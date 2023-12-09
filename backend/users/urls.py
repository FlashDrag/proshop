from django.urls import path

from . import views

urlpatterns = [
    path(
        "login/",
        views.TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("profile/", views.getUserProfile, name="user-profile"),
]
