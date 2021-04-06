from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from apps.feed.forms import FeedRegisterForm
from apps.feed.models import Feed
from apps.users.models import User
from .base import BaseDetailView
from apps.feed.task import update_feed


def home(request):
    return redirect('user:register')


class UserFeed(UserPassesTestMixin, BaseDetailView):
    model = User
    template_name = 'feed/user_feeds.html'
    login_url = reverse_lazy('user:login')
    context_object_name = 'user'

    def test_func(self):
        return self.request.user.id == self.kwargs['pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feeds'] = self.get_feeds()

        # queje = update_feed.delay(context['feeds'])

        return context


class FeedDetail(BaseDetailView):
    model = Feed
    template_name = 'feed/feed_detail.html'
    login_url = reverse_lazy('user:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feeds'] = self.get_feeds()
        url = context['object'].url
        context['feed_obj'] = next(feed for feed in context['feeds'] if feed.get(
            'source').get('url') == url)

        return context


class FeedRegister(LoginRequiredMixin, CreateView):
    model = Feed
    form_class = FeedRegisterForm
    template_name = 'feed/register_feed.html'
    login_url = reverse_lazy('user:login')

    def form_valid(self, form):
        user = User.objects.get(id=self.request.user.id)
        form.instance.user = user
        return super(FeedRegister, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'feed:user_feed', kwargs={
                'pk': self.request.user.id})


class FeedDelete(UserPassesTestMixin, DeleteView):
    model = Feed
    form_class = FeedRegisterForm
    template_name = 'feed/delete_feed.html'
    login_url = reverse_lazy('user:login')

    def test_func(self):
        feed = self.model.objects.get(id=self.kwargs['pk'])
        return self.request.user.id == feed.user.id

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        feed = Feed.objects.filter(pk=self.object.id)
        feed.delete()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse_lazy(
            'feed:user_feed', kwargs={
                'pk': self.request.user.id})
