from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from inventory.forms import InventoryForm
from inventory.models import Item, ItemCategory


class InventoryOverview(LoginRequiredMixin, TemplateView):
    template_name = 'inventory_overview.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category_list'] = ItemCategory.objects.all()
        ctx['object_list'] = Item.objects.filter(stock__gt=0)[:6]
        ctx['out_of_stock'] = Item.objects.filter(stock=0).count()
        return ctx


class InventoryAddEditMixin:
    model = Item
    form_class = InventoryForm
    template_name = 'inventory_form.html'

    def post(self, *args, **kwargs):
        self.save_type = 'add_another' if 'add_another' in self.request.POST else 'save'
        return super().post(*args, **kwargs)

    def get_success_url(self):
        if self.save_type == 'add_another':
            return reverse('inventory:inventory_add')
        return reverse('inventory:inventory_overview')


class InventoryAddView(LoginRequiredMixin, InventoryAddEditMixin, CreateView):
    pass


class InventoryUpdateView(LoginRequiredMixin, InventoryAddEditMixin, UpdateView):
    def get_form_kwargs(self):
        kw = super().get_form_kwargs()
        kw['initial'] = {
            'category': self.object.id
        }
        return kw


class InventoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'inventory_delete.html'
    success_url = reverse_lazy('inventory:inventory_overview')


class OutofStockItems(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'out_of_stock.html'

    def get_queryset(self):
        return super().get_queryset().exclude(stock__gt=0)
