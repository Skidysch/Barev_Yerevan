from django.urls import path

from .views import HomeView, CategoryView, PlaceView, SearchView

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
    path('search/', SearchView.as_view(), name='search'),
]
