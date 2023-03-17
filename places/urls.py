from django.urls import path

from .views import HomeView, CategoryView, PlaceView, \
    SigninView, SignupView, ResetView, SearchView, signout, change_user

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path(
        'categories/<slug:category_slug>',
        CategoryView.as_view(),
        name='category'
    ),
    path(
        'place/<slug:place_slug>',
        PlaceView.as_view(),
        name='place'
    ),
    path('auth/signin/', SigninView.as_view(), name='signin'),
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('auth/reset/', ResetView.as_view(), name='reset'),
    path('auth/signout/', signout, name='signout'),
    path('auth/chuser/', change_user, name='chuser'),
    path('search/', SearchView.as_view(), name='search'),
]
