import csv

from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.response import Response


class ApiMixin:
    """Класс-миксин для классов представлений. Получает на вход текущую модель и сериализатор,
    и выполняет GET, POST, PUT, DELETE для выбранных записейgi"""
    def __init__(self, serializer, model):
        self.serializer = serializer
        self.model = model

    def get_object(self, pk=None):
        if pk:
            try:
                return self.model.objects.get(pk=pk)
            except self.model.DoesNotExist:
                raise Http404
        else:
            try:
                return self.model.objects.all()
            except self.model.DoesNotExist:
                raise Http404

    def get(self, request, pk=None):
        if pk:
            query = self.get_object(pk)
            return Response(self.serializer(query, many=False).data)
        else:
            query = self.get_object()
            return Response(self.serializer(query, many=True).data)

    def post(self, request, pk):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if request.user.is_staff:
            query = self.get_object(pk)
            serializer = self.serializer(query,
                                         data=request.data,
                                         partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('Доступ запрещен!', status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        if request.user.is_staff:
            query = self.get_object(pk)
            query.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('Доступ запрещен!', status=status.HTTP_403_FORBIDDEN)


class CsvMixin:
    """Класс-миксин. Записывает JSON данные от сериализатора в CSV файл и возвращает его пользователю"""
    def __init__(self, serializer, model):
        self.serializer = serializer
        self.model = model

    def get(self, request, pk=None):
        response = HttpResponse(content_type='text/csv')
        if pk:
            query = self.serializer(self.get_queryset(pk)).data
        else:
            query = self.serializer(self.get_queryset(), many=True).data
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        writer = csv.DictWriter(response, fieldnames=query.keys())
        writer.writeheader()
        writer.writerow(query)
        return response

    def get_queryset(self, pk=None):
        if pk:
            try:
                return self.model.objects.get(pk=pk)
            except self.model.DoesNotExist:
                raise Http404
        else:
            try:
                return self.model.objects.all()
            except self.model.DoesNotExist:
                raise Http404
