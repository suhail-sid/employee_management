from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination


class EmployeePagination(PageNumberPagination):
    page_size = 10 


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()  
    serializer_class = EmployeeSerializer  
    pagination_class = EmployeePagination 
    permission_classes = [IsAuthenticated] 
    filter_backends = [filters.SearchFilter] 
    search_fields = ['department', 'role'] 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        self.perform_create(serializer) 
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  
        self.perform_destroy(instance)  
        return Response(status=status.HTTP_204_NO_CONTENT) 
