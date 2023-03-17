from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView

from .forms import SigninForm, SignupForm, SearchForm
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
        c_def = self.get_user_context(title=f'Category - {category.name}', category=category)
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


class SigninView(ContextMixin, LoginView):
    form_class = SigninForm
    template_name = 'places/signin.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign in')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('home')


class SignupView(ContextMixin, generic.CreateView):
    form_class = SignupForm
    template_name = 'places/signup.html'
    success_url = reverse_lazy('signin')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign up')
        return dict(list(context.items()) + list(c_def.items()))

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return redirect('home')


class ResetView(ContextMixin, generic.TemplateView):
    template_name = 'places/reset.html'


def signout(request):
    logout(request)
    return redirect('home')


def change_user(request):
    logout(request)
    return redirect('signin')


class SearchView(ContextMixin, generic.ListView):
    template_name = 'places/search.html'
    context_object_name = 'places'

    def get_queryset(self):
        return Place.objects.filter(name__icontains=self.request.GET.get('query'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query')
        c_def = self.get_user_context(title='Search results')
        return dict(list(context.items()) + list(c_def.items()))
