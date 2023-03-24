from .forms import SearchForm
from .models import Category


class ContextMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.all()
        search_form = SearchForm()

        context['categories'] = categories
        context['search_form'] = search_form

        return context
