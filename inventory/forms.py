from django import forms

from inventory.models import Item, ItemCategory


class SelectizeFormMixin:
    # pass

    def get_value(self, name):
        field = self.fields.get(name)
        if field:
            return field.widget.value_from_datadict(self.data, self.files, self.add_prefix(name))

    def full_clean(self):
        if self.data:
            self.data = self.data.copy()
            for name, field in self.fields.items():
                if name in self.Meta.selectize_create:
                    value = self.get_value(name)
                    if value and value.startswith('_'):
                        kwargs = {'name': value.strip('_')}
                        obj, __ = field.queryset.model.objects.get_or_create(**kwargs)
                        self.data[name] = obj.id
        super().full_clean()


class InventoryForm(SelectizeFormMixin, forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=ItemCategory.objects.all(),
        widget=forms.Select(attrs={'data-add-new': 'true'})
    )

    class Meta:
        model = Item
        fields = ('category', 'product_id', 'name', 'company', 'price', 'stock')
        selectize_create = ['category']
