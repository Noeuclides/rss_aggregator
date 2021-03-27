from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView)

from apps.feed.forms import FeedRegisterForm
from apps.feed.models import Feed
from apps.users.models import User


def home(request):
    return render(request, 'feed/home.html')


class FeedList(LoginRequiredMixin, ListView):
    model = Feed
    template_name = 'feed/feed_list.html'
    login_url = reverse_lazy('users:login')
    context_object_name = 'feed_obj'

    def get_queryset(self):
        return self.model.objects.select_related('owner', 'company')


class FeedOwnerList(UserPassesTestMixin, DetailView):
    model = User
    template_name = 'feed/user_properties.html'
    login_url = reverse_lazy('users:login')
    context_object_name = 'owner'

    def test_func(self):
        return self.request.user.id == self.kwargs['pk']


    def get_context_data(self, **kwargs):
        context = super(FeedOwnerList, self).get_context_data(**kwargs)
        properties = feed.objects.filter(owner=self.request.user)

        context['feed_obj'] = properties

        return context


class FeedRegister(LoginRequiredMixin, CreateView):
    model = Feed
    form_class = FeedRegisterForm
    template_name = 'feed/register_feed.html'
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = User.objects.get(id=self.request.user.id)
        form.instance.owner = user
        return super(FeedRegister, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('feed:owner_properties', kwargs={'pk': self.request.user.id})


class feedDelete(UserPassesTestMixin, DeleteView):
    model = Feed
    form_class = FeedRegisterForm
    template_name = 'feed/delete_feed.html'
    login_url = reverse_lazy('users:login')

    def test_func(self):
        feed = self.model.objects.get(id=self.kwargs['pk'])
        return self.request.user.id == feed.owner.id

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        feed = feed.objects.filter(pk=self.object.id)
        feed.delete()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse_lazy('feed:owner_properties', kwargs={'pk': self.request.user.id})

