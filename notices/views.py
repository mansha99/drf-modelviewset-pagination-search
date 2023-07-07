from .models import Notice
from .serializers import NoticeSerializer
from rest_framework import viewsets
from .pagination import CustomPagination
from rest_framework.exceptions import ValidationError

class NoticeModelViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        kw = self.request.query_params.get('kw')
        if kw is not None:
            queryset = queryset.filter(title__contains=kw)
        order = self.request.query_params.get('order')
        if order is not None:
            fields = ['id', '-id','title','title']
            if order in fields:
                queryset = queryset.order_by(order)
            else:
                raise ValidationError({'errror': 'order field must be in ' + ', '.join(fields)})
        return queryset
