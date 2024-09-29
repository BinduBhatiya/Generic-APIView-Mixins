from django.shortcuts import render
from .models import student
from .serializers import studentserializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# Create your views here.
# list & create : id is not required
class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = student.objects.all()
    serializer_class = studentserializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 
    

# retrive, update and destroy : id is required
class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = student.objects.all()
    serializer_class = studentserializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) 
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 
    