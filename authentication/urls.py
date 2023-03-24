from django.urls import path

from .views import SigninView, SignupView, ResetView, signout, change_user

urlpatterns = [
    path('signin/', SigninView.as_view(), name='signin'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('reset/', ResetView.as_view(), name='reset'),
    path('signout/', signout, name='signout'),
    path('chuser/', change_user, name='chuser'),
]
