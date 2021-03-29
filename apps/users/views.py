from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormView

from apps.users.forms import LoginForm, RegisterForm
from apps.users.models import User


class Login(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        return super(Login, self).form_invalid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('feed:user_feed', kwargs={'pk': self.request.user.id})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user/login')


class UserRegister(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/registration.html'

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=email, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse('feed:user_feed', kwargs={'pk': user.id}))
