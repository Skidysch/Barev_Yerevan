from django.views import generic

from .mixins import ContextMixin
from .models import Place, Category


class HomeView(ContextMixin, generic.ListView):
    model = Category
    template_name = 'places/index.html'
    context_object_name = 'cats'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Barev Yerevan')
        return dict(list(context.items()) + list(c_def.items()))


class CategoryView(ContextMixin, generic.ListView):
    model = Place
    template_name = 'places/category.html'
    context_object_name = 'places'

    def get_queryset(self):
        return Place.objects.prefetch_related('categories').filter(
            categories__slug=self.kwargs['category_slug'],
            is_published=True
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(
            title=f'Category - {category.name}',
            category=category)

        return dict(list(context.items()) + list(c_def.items()))


class PlaceView(ContextMixin, generic.DetailView):
    model = Place
    template_name = 'places/place.html'
    slug_url_kwarg = 'place_slug'
    context_object_name = 'place'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['place'])
        return dict(list(context.items()) + list(c_def.items()))


class SearchView(ContextMixin, generic.ListView):
    template_name = 'places/search.html'
    context_object_name = 'places'

    def get_queryset(self):
        return Place.objects.filter(
            name__icontains=self.request.GET.get('query')
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query')
        c_def = self.get_user_context(title='Search results')
        return dict(list(context.items()) + list(c_def.items()))
