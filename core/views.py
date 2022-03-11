from django.test import TestCase
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from core.models import EquityStockWatch
from core.serializers import EquityStockWatchSerializer

# Create your views here.


class EquityStockWatchViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin,
                              mixins.RetrieveModelMixin):
    queryset = EquityStockWatch.objects.all().order_by("-id")
    serializer_class = EquityStockWatchSerializer

    def get_queryset(self):
        return self.queryset

    def retrieve(self, request, *args, **kwargs):
        symbol = self.kwargs["pk"]
        print(symbol)
        instance = self.queryset.filter(symbol__iexact=symbol)
        if not len(instance):
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        instance = instance[0]  # latest

        if self.request.GET.get("filter"):
            query_filter = self.request.GET.get("filter")
            data ={query_filter: getattr(instance, query_filter)}
        else:
            data = self.get_serializer(instance).data
        return Response(data)


class EquityStockWatchWithAnalyticsViewset(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = EquityStockWatch.objects.all()
    serializer_class = EquityStockWatchSerializer

    def get_queryset(self):
        level_filter = self.request.GET.get("filter")
        filter_param = self.request.GET.get("param")

        if level_filter == "low":
            queryset = self.queryset.order_by(filter_param)
        else:
            queryset = self.queryset.order_by(f"-{filter_param}")
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if len(queryset):
            filter_param = self.request.GET.get("param")
            queryset = queryset[0]
            queryset = {"symbol": queryset.symbol, filter_param: getattr(queryset, filter_param)}

        return Response(queryset, status=status.HTTP_200_OK)