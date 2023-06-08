from requests import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from .models import Booking, Menu
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated


# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
#
# token = Token.objects.create(user=...)
# print(token.key)
#
#
# @api_view
# @permission_classes([IsAuthenticated])
# def securedView(request):
#     return Response({"message": "need authentication"})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
