from rest_framework import serializers
from .models import Doctor, Degree

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'user_id', 'wage', 'specialist_id', 'created_at', 'updated_at']

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.wage = validated_data.get('wage', instance.wage)
        instance.specialist_id = validated_data.get('specialist_id', instance.specialist_id)
        instance.save()
        return instance

class DegreeSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = Degree
        fields = ['id', 'degree_name', 'institution_name', 'date_awarded', 'description', 'doctor']

    def create(self, validated_data):
        doctor = validated_data.pop('doctor', None)
        if doctor:
            doctor_instance = Doctor.objects.filter(id=doctor.id, is_active=True).first()
            if doctor_instance:
                validated_data['doctor'] = doctor_instance
            else:
                raise serializers.ValidationError('Doctor does not exist')
        return Degree.objects.create(**validated_data)

    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        doctor = validated_data.pop('doctor', None)
        if doctor:
            doctor_instance = Doctor.objects.filter(id=doctor.id, is_active=True).first()
            if doctor_instance:
                instance.doctor = doctor_instance
            else:
                raise serializers.ValidationError('Doctor does not exist')

        instance.degree_name = validated_data.get('degree_name', instance.degree_name)
        instance.institution_name = validated_data.get('institution_name', instance.institution_name)
        instance.date_awarded = validated_data.get('date_awarded', instance.date_awarded)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class DoctorListSerializer(serializers.ModelSerializer):
    degrees = DegreeSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'user_id', 'wage', 'specialist_id', 'created_at', 'updated_at', 'degrees']
