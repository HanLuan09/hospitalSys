from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee, Position
from .serializers import EmployeeSerializer, PositionSerializer, EmployeeReadSerializer

class CreateEmployeeView(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreatePositionView(APIView):
    def post(self, request):
        serializer = PositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeListView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeReadSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PositionListView(APIView):
    def get(self, request):
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class EmployeeDetailView(APIView):
    def get(self, request, id):
        employees = Employee.objects.get(id = id)
        serializer = EmployeeReadSerializer(employees)
        return Response(serializer.data, status=status.HTTP_200_OK)
