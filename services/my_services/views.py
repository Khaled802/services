

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BankSerializer, LocationSerializer, SevicesSerializer
from .models import Bank, BaseService

# Create your views here.



class ServicesByLocation(APIView):
    '''
    get all services by the location
    '''
    @staticmethod
    def is_all_services_empty(services: dict) -> bool:
        for result in services.values():
            if result:
                return False
        return True
    
    def get(self, request):
        # using custome serializer to get each service with its result
        serialized_services = SevicesSerializer.get_by_location(request)
        if self.is_all_services_empty(serialized_services):
            return Response({'detail': 'no such a loction'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data={'services': serialized_services}, status=status.HTTP_200_OK)


class BankViewList(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankViewObject(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer



