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


class ItemCategoryListView(LoginRequiredMixin, ListView):
    model = ItemCategory
    template_name = 'category_list.html'


class ItemCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ItemCategory
    template_name = 'category_form.html'
    fields = ('name', )
    success_url = reverse_lazy('inventory:category_list')


class ItemCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ItemCategory
    template_name = 'category_delete.html'
    success_url = reverse_lazy('inventory:category_list')


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'item_list.html'

    def get_queryset(self, **kwargs):
        cat_id = self.kwargs.get('cat_id', None)
        filter_kwargs = {'category_id': cat_id} if cat_id else {}
        return super().get_queryset(**kwargs).filter(**filter_kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.kwargs.get('cat_id', None):
            ctx['category'] = ItemCategory.objects.get(id=self.kwargs['cat_id'])
        return ctx