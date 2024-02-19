from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=100, verbose_name='Страна')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.country_name


class Producer(models.Model):
    producer_name = models.CharField(max_length=100, verbose_name='Производитель')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='producers', verbose_name='Страна')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.producer_name


class Car(models.Model):
    car_name = models.CharField(max_length=100, verbose_name='Автомобиль')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='cars', verbose_name='Производитель')
    released_at = models.DateField(verbose_name='Дата начала выпуска', null=True)
    release_ended = models.DateField(verbose_name='Дата окончания выпуска', null=True, blank=True)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return self.car_name


class Comment(models.Model):
    email = models.EmailField(verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    text = models.TextField(verbose_name='Комментарий')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments', verbose_name='Автомобиль')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'

    def __str__(self):
        return f'Комментарий "{self.text[:20]}..." от {self.email}'
