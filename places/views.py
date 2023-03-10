from django.views import generic

from .mixins import ContextMixin
from .models import Place, Category


class HomeView(ContextMixin, generic.ListView):
    model = Place
    template_name = 'places/index.html'
    context_object_name = 'places'

    def get_queryset(self):
        return Place.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Barev Yerevan')
        return dict(list(context.items()) + list(c_def.items()))


class CategoryView(ContextMixin, generic.ListView):
    model = Category
    template_name = 'places/index.html'
    context_object_name = 'places'

    def get_queryset(self):
        return Place.objects.filter(
            categories__slug=self.kwargs['category_slug'],
            is_published=True
        ).prefetch_related('categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title=f'{category.name}')
        return dict(list(context.items()) + list(c_def.items()))
