from rest_framework import serializers
from .models import Patient, Insurance

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'use_id', 'first_name', 'last_name', 'birth_date', 'sex', 'address', 'phone_number']

    def destroy(self, instance):
        instance.save()
        return instance

    
class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'birth_date', 'sex', 'address', 'phone_number']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.address = validated_data.get('address', instance.address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance

class InsuranceSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    class Meta:
        model = Insurance
        fields = ['code', 'patient', 'provider', 'update_date', 'effective_date', 'expiration_date']

    def create(self, validated_data):
        return Insurance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.provider = validated_data.get('provider', instance.provider)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.effective_date = validated_data.get('effective_date', instance.effective_date)
        instance.expiration_date = validated_data.get('expiration_date', instance.expiration_date)
        instance.save()
        return instance
