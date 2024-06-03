from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext as _
from django.contrib import messages

from .filters import AdFilter
from .forms import AdForm
from .models import Ad


PAGINATE_BY = 2


class AdBoardView(ListView):
    model = Ad
    ordering = '-date_published'
    template_name = 'ad_board/ad_board.html'
    context_object_name = 'ad_list'
    paginate_by = PAGINATE_BY

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class AdDetailView(DetailView):
    model = Ad
    template_name = 'ad_board/ad_detail.html'
    context_object_name = 'ad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.can_view(self.request.user):
            raise PermissionDenied
        return obj


class AdCreateView(LoginRequiredMixin, CreateView):
    form_class = AdForm
    model = Ad
    template_name = 'ad_board/ad_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        return context


class AdUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AdForm
    model = Ad
    template_name = 'ad_board/ad_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def ad_delete(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.user == ad.user or request.user.is_staff:
        ad.delete()
        messages.success(request, _('Ad has been deleted successfully.'))
        return redirect('ad_board')
    else:
        messages.error(request, _('You do not have permission to delete this ad.'))
        return redirect('ad_detail', pk=pk)



@login_required
@require_POST
def ad_publish(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.user == ad.user or request.user.is_staff:
        ad.publish_ad()
        messages.success(request, _('Ad has been published successfully.'))
    else:
        messages.error(request, _('You do not have permission to publish this ad.'))
    return redirect('ad_detail', pk=pk)


@login_required
@require_POST
def ad_unpublish(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.user == ad.user or request.user.is_staff:
        ad.unpublish_ad()
        messages.success(request, _('Ad has been unpublished successfully.'))
    else:
        messages.error(request, _('You do not have permission to unpublish this ad.'))
    return redirect('ad_detail', pk=pk)