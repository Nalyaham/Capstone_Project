from .models import Review, CustomUser
from .serializers import ReviewSerializer, UserSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
from rest_framework.exceptions import PermissionDenied

class RegistrationView(generics.CreateAPIView):
    queryset= CustomUser.objects.all()
    serializer_class= UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"detail": "Registration successful"})
        except IntegrityError:
            return Response({"error": "Username already exists"}, status=400)
        
class SubmitView(generics.CreateAPIView):
    queryset= Review.objects.all()
    serializer_class= ReviewSerializer

    def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"detail": "Submission successful"})

class UpdateReview(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer 
    lookup_field = 'pk'


class DeleteReview(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'pk'

class ListReview(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
        

        
        



    

