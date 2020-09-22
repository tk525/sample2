from django_filters import filters
from django_filters import FilterSet
from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （under）'


class ItemFilter(FilterSet):

    name = filters.CharFilter(label='name', lookup_expr='contains')
    memo = filters.CharFilter(label='add information', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
            ('age', 'age'),
        ),
        field_labels={
            'name': 'name',
            'age': 'age',
        },
        label='sort'
    )

    class Meta:

        model = Item
        fields = ('name', 'sex', 'memo',)
