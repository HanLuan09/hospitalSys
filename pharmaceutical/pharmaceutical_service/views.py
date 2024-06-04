import requests
from djongo.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Category, Pharmaceutical, Supplier
from .serializers import CategorySerializer, SupplierSerializer, PharmaceuticalSerializer, PharmaceuticalListSerializer

class CreateCategoryView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CreateSupplierView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CreatePharmaceuticalView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        
        serializer = PharmaceuticalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SupplierListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        suppliers = Supplier.objects.filter(is_active__in=[True]).all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        categories = Category.objects.filter(is_active__in=[True]).all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PharmaceuticalListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        pharmaceuticals = Pharmaceutical.objects.filter(is_active__in=[True]).all()
        serializer = PharmaceuticalListSerializer(pharmaceuticals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PharmaceuticalOfCategoryListView(APIView):
    permission_classes = [AllowAny]
       
    def get(self, request, category_id):
        pharmaceuticals = Pharmaceutical.objects.filter(is_active__in=[True], category_id = category_id).all()
        serializer = PharmaceuticalListSerializer(pharmaceuticals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class SupplierDetailView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, id):
        try:
            supplier = Supplier.objects.get(id = id)
        except Supplier.DoesNotExist:
            return Response({'error': 'supplier not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            supplier = Supplier.objects.get(id = id)
        except Supplier.DoesNotExist:
            return Response({'error': 'Supplier not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SupplierSerializer()
        serializer.destroy(supplier)
        return Response({'message': 'Supplier deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class CategoryDetailView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, id):
        try:
            category = Category.objects.get(id = id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            category = Category.objects.get(id = id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer()
        serializer.destroy(category)
        return Response({'message': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class PharmaceuticalDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        try:
            pharmaceutical = Pharmaceutical.objects.get(id = id)
        except Pharmaceutical.DoesNotExist:
            return Response({'error': 'pharmaceutical not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PharmaceuticalListSerializer(pharmaceutical)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            pharmaceutical = Pharmaceutical.objects.get(id = id)
        except Pharmaceutical.DoesNotExist:
            return Response({'error': 'Pharmaceutical not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PharmaceuticalSerializer(pharmaceutical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            pharmaceutical = Pharmaceutical.objects.get(id = id)
        except Pharmaceutical.DoesNotExist:
            return Response({'error': 'Pharmaceutical not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PharmaceuticalSerializer()
        serializer.destroy(pharmaceutical)
        return Response({'message': 'Pharmaceutical deleted successfully'}, status=status.HTTP_204_NO_CONTENT)





