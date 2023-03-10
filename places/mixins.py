from django.core.cache import cache

# from .forms import ContactForm
from .models import Category


class ContextMixin:
    shut_up = True

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = cache.get('categories')
        if not categories:
            categories = Category.objects.all()
            cache.set('categories', categories, 60)
        # form = cache.get('form')
        # if not form:
        #     form = ContactForm()
        #     cache.set('form', form, 60)

        context['categories'] = categories
        # context['form'] = form

        return context
