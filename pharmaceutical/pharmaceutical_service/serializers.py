from rest_framework import serializers
from .models import Category, Pharmaceutical, Supplier

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'des']

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
    
class UpdateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'des']
        
    def update(self, instance, validated_data):

        instance.name = validated_data.get('name')
        instance.des = validated_data.get('des')
        instance.is_active = False
        instance.save()
        return instance

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id' ,'name', 'address', 'des']

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
    
    def update(self, instance, validated_data):

        instance.name = validated_data.get('name')
        instance.address = validated_data.get('address')
        instance.des = validated_data.get('des')
        instance.is_active = False
        instance.save()
        return instance
    
class PharmaceuticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmaceutical
        fields = ['id', 'name', 'quantity', 'price', 'description', 'origin', 'expiry_date', 'manufacturing_date', 'category', 'supplier']

    def create(self, validated_data):

        category = validated_data.pop('category', None)
        supplier = validated_data.pop('supplier', None)

        if category:
            category_id = category.id
            category_instance = Category.objects.filter(is_active__in=[True], id=category_id).first()
            if category_instance:
                validated_data['category'] = category_instance
            else:
                raise serializers.ValidationError('Category does not exits')
        
        if supplier:
            supplier_id = supplier.id
            supplier_instance = Supplier.objects.filter(is_active__in=[True], id=supplier_id).first()
            if supplier_instance:
                validated_data['supplier'] = supplier_instance
            else:
                raise serializers.ValidationError('supplier does not exist')
            
        return Pharmaceutical.objects.create(**validated_data)
    
    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        category = validated_data.pop('category', None)
        supplier = validated_data.pop('supplier', None)
        
        if category:
            category_id = category.id
            category_instance = Category.objects.filter(is_active__in=[True], id=category_id).first()
            if category_instance:
                validated_data['category'] = category_instance
            else:
                raise serializers.ValidationError('Category does not exits')
        
        if supplier:
            supplier_id = supplier.id
            supplier_instance = Supplier.objects.filter(is_active__in=[True], id=supplier_id).first()
            if supplier_instance:
                validated_data['supplier'] = supplier_instance
            else:
                raise serializers.ValidationError('supplier does not exist')
            

        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.origin = validated_data.get('origin', instance.origin)
        instance.expiry_date = validated_data.get('expiry_date', instance.expiry_date)
        instance.manufacturing_date = validated_data.get('manufacturing_date', instance.manufacturing_date)

        instance.save()
        return instance
    
class PharmaceuticalListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    supplier = SupplierSerializer()

    class Meta:
        model = Pharmaceutical
        fields = ['id', 'name', 'quantity', 'price', 'description', 'origin', 'expiry_date', 'manufacturing_date', 'category', 'supplier']


    
