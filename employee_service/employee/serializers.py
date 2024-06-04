from rest_framework import serializers
from .models import Employee, Position

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name', 'description']

class EmployeeReadSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'user_id', 'specialist_id', 'created_at', 'updated_at', 'position']


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'user_id', 'specialist_id', 'created_at', 'updated_at', 'position']

    def create(self, validated_data):
        position = validated_data.pop('position')
        if position:
            position_instance = Position.objects.filter(id=position.id, is_active=True).first()
            if position_instance:
                validated_data['position'] = position_instance
            else:
                raise serializers.ValidationError('position does not exist')
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        position_data = validated_data.pop('position')
        instance.position.name = position_data.get('name', instance.position.name)
        instance.position.description = position_data.get('description', instance.position.description)
        instance.position.save()

        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.specialist_id = validated_data.get('specialist_id', instance.specialist_id)
        instance.save()

        return instance
