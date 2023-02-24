from django.urls import path

from .views import BankViewList, BankViewObject, ServicesByLocation




urlpatterns = [
    path('bank/', BankViewList.as_view()),
    path('bank/<int:id>/', BankViewObject.as_view()),
    path('search/location/', ServicesByLocation.as_view()),
]