from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import SigninForm, SignupForm
from .mixins import ContextMixin


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
