import django_filters
from business.models import Transact, Comment
from django.contrib.auth.models import User

class TransactFilter(django_filters.FilterSet):

    class Meta:
        model = Transact
        # # fields = '__all__'
        # fields = {'current_class': ['exact']}
        fields = {'subject',}

class MyTransactFilter(django_filters.FilterSet):

    class Meta:
        model = Transact
        # # fields = '__all__'
        # fields = {'current_class': ['exact']}
        fields = {'subject'}

class Commentilter(django_filters.FilterSet):

    class Meta:
        model = Comment
        # # fields = '__all__'
        # fields = {'current_class': ['exact']}
        fields = {'required_amount', 'author', 'date_added',}


class TransactReportFilter(django_filters.FilterSet):

    class Meta:
        model = Transact
        # # fields = '__all__'
        # fields = {'current_class': ['exact']}
        fields = {'created_by', }

class TransactSummaryFilter(django_filters.FilterSet):

    class Meta:
        model = Transact
        # # fields = '__all__'
        # fields = {'current_class': ['exact']}
        fields = {'created_by__username', }
        

