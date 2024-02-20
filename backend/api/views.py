from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from .models import Country, Producer, Car, Comment
from .serializers import (CountrySerializer, CountryDetailSerializer, ProducerDetailSerializer,
                          CarDetailSerializer, CommentSerializer)

from .utils import ApiMixin, CsvMixin


class CountryListApiView(ApiMixin, APIView):
    def __init__(self):
        super().__init__(serializer=CountrySerializer, model=Country)

    def get(self, request, pk=None):
        return super().get(request, pk)

    def post(self, request, pk=None):
        if request.user.is_staff:
            return super().post(request, pk)
        return Response('Доступ запрещен!',status=status.HTTP_403_FORBIDDEN)


class CountryToXlsApiView(XLSXFileMixin, generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    renderer_classes = [XLSXRenderer]
    filename = 'countries.xlsx'


class CountryToCsvApiView(CsvMixin,  APIView):
    def __init__(self):
        super().__init__(serializer=CountrySerializer, model=Country)


class CountryDetailApiView(ApiMixin, APIView):
    def __init__(self):
        super().__init__(serializer=CountryDetailSerializer, model=Country)

    def get(self, request, pk):
        return super().get(request, pk)

    def put(self, request, pk):
        return super().put(request, pk)

    def delete(self, request, pk):
        return super().delete(request, pk)


class CountryDetailToXlsApiView(XLSXFileMixin, generics.ListAPIView):
    serializer_class = CountryDetailSerializer
    renderer_classes = [XLSXRenderer]
    filename = f"country.xlsx"

    def get_queryset(self):
        return Country.objects.filter(pk=self.kwargs['pk'])


class CountryDetailToCsvApiView(CsvMixin, APIView):
    def __init__(self):
        super().__init__(serializer=CountryDetailSerializer, model=Country)


class ProducerDetailApiView(ApiMixin, APIView):
    def __init__(self):
        super().__init__(serializer=ProducerDetailSerializer, model=Producer)

    def get(self, request, pk):
        return super().get(request, pk)

    def post(self, request, pk):
        if request.user.is_staff:
            return super().post(request, pk)
        return Response('Доступ запрещен!', status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk):
        return super().put(request, pk)

    def delete(self, request, pk):
        return super().delete(request, pk)


class ProducerDetailToXlsApiView(XLSXFileMixin, generics.RetrieveAPIView):
    serializer_class = ProducerDetailSerializer
    renderer_classes = [XLSXRenderer]
    filename = f"producer.xlsx"

    def get_queryset(self):
        return Producer.objects.filter(pk=self.kwargs['pk'])


class ProducerDetailToCsvApiView(CsvMixin, APIView):
    def __init__(self):
        super().__init__(serializer=ProducerDetailSerializer, model=Producer)


class CarDetailApiView(ApiMixin, APIView):
    def __init__(self):
        super().__init__(serializer=CarDetailSerializer, model=Car)

    def get(self, request, pk):
        return super().get(request, pk)

    def post(self, request, pk):
        if request.user.is_staff:
            return super().post(request, pk)
        return Response('Доступ запрещен!', status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk):
        return super().put(request, pk)

    def delete(self, request, pk):
        return super().delete(request, pk)


class CarDetailToXlsApiView(XLSXFileMixin, generics.ListAPIView):
    serializer_class = CarDetailSerializer
    renderer_classes = [XLSXRenderer]
    filename = f"car.xlsx"

    def get_queryset(self):
        return Car.objects.filter(pk=self.kwargs['pk'])


class CarDetailToCsvApiView(CsvMixin, APIView):
    def __init__(self):
        super().__init__(serializer=CarDetailSerializer, model=Car)


class CommentDetailView(ApiMixin, APIView):
    def __init__(self):
        super().__init__(serializer=CommentSerializer, model=Comment)

    def get(self, request, pk):
        return super().get(request, pk)

    def post(self, request, pk):
        return super().post(request, pk)

    def put(self, request, pk):
        return super().put(request, pk)

    def delete(self, request, pk):
        return super().delete(request, pk)


class CommentToXlsApiView(XLSXFileMixin, generics.ListAPIView):
    serializer_class = CommentSerializer
    renderer_classes = [XLSXRenderer]
    filename = f"comment.xlsx"

    def get_queryset(self):
        return Comment.objects.filter(pk=self.kwargs['pk'])


class CommentToCsvApiView(CsvMixin,APIView):
    def __init__(self):
        super().__init__(serializer=CommentSerializer, model=Comment)
