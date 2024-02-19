from django.db.models import Count
from rest_framework import serializers

from .models import Country, Producer, Car, Comment


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class CountryDetailSerializer(serializers.ModelSerializer):
    producers = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='producer_name'
    )

    class Meta:
        model = Country
        fields = ['country_name', 'producers']


class ProducerDetailSerializer(serializers.ModelSerializer):
    country_name = serializers.ReadOnlyField(source='country.country_name')
    cars = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='car_name'
    )
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = Producer
        fields = ['country', 'country_name', 'cars', 'total_comments']

    def get_total_comments(self, obj):
        '''Возвращает количество комментариев к машинам выбранного производителя'''
        return Car.objects.filter(producer=obj).aggregate(total_comments=Count('comments'))


class CarDetailSerializer(serializers.ModelSerializer):
    total_comments = serializers.SerializerMethodField(read_only=True)
    producer_name = serializers.ReadOnlyField(source='producer.producer_name')

    def get_total_comments(self, Car):
        '''Возвращает общее кол-во комментариев для этого автомобиля'''
        return Car.comments.count()

    class Meta:
        model = Car
        fields = ['producer', 'producer_name', 'car_name', 'total_comments']


class CommentSerializer(serializers.ModelSerializer):
    car_name = serializers.ReadOnlyField(source='car.car_name')

    class Meta:
        model = Comment
        fields = ['email', 'text', 'car', 'car_name']
