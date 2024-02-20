from django.urls import include, path, re_path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from . import views

app_name = "api"

urlpatterns = [
    # страны
    path("countries/", views.CountryListApiView.as_view(), name="countries"),
    path("countries/xlsx", views.CountryToXlsApiView.as_view(), name="countries_xlsx"),
    path("countries/csv", views.CountryToCsvApiView.as_view(), name="countries_csv"),

    # подробный просмотр информации о конкретной стране
    path("country/<int:pk>", views.CountryDetailApiView.as_view(), name="country"),
    path("country/<int:pk>/xlsx", views.CountryDetailToXlsApiView.as_view(), name="country_xlsx"),
    path("country/<int:pk>/csv", views.CountryDetailToCsvApiView.as_view(), name="country_csv"),

    # производитель
    path("producer/<int:pk>", views.ProducerDetailApiView.as_view(), name="producer"),
    path("producer/<int:pk>/xlsx", views.ProducerDetailToXlsApiView.as_view(), name="producer_xlsx"),
    path("producer/<int:pk>/csv", views.ProducerDetailToCsvApiView.as_view(), name="producer_csv"),

    # автомобили
    path("car/<int:pk>", views.CarDetailApiView.as_view(), name="car"),
    path("car/<int:pk>/xlsx", views.CarDetailToXlsApiView.as_view(), name="car_xlsx"),
    path("car/<int:pk>/csv", views.CarDetailToCsvApiView.as_view(), name="car_csv"),

    # комментарии
    path("comment/<int:pk>", views.CommentDetailView.as_view(), name="comment"),
    path("comment/<int:pk>/xlsx", views.CommentToXlsApiView.as_view(), name="comment_xlsx"),
    path("comment/<int:pk>/csv", views.CommentToCsvApiView.as_view(), name="comment_csv"),

    # JWT и авторизация
    path("auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
