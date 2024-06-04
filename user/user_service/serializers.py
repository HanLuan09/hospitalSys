from rest_framework import serializers
from .models import User, UserAddress, UserProfile
from django.contrib.auth.hashers import make_password, check_password


class UserProfileRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'dob']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = UserProfileRegisterSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'phone', 'password', 'profile']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        profile_data = validated_data.pop('profile', None)
        user = User.objects.create(**validated_data)
        if profile_data:
            UserProfile.objects.create(user=user, **profile_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'dob']

    def create(self, validated_data):
        # Lấy người dùng từ request
        user = self.context['request'].user
        # Thêm người dùng vào dữ liệu đã xác thực
        validated_data['user'] = user
        # Tạo UserProfile với dữ liệu đã xác thực
        return UserProfile.objects.create(**validated_data)

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['id', 'apartment_number', 'street', 'city', 'province', 'des']

    def create(self, validated_data):
        # Lấy người dùng từ request
        user = self.context['request'].user
        validated_data['user'] = user
        return UserAddress.objects.create(**validated_data)
    
class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True) 

    def validate(self, data):
        phone = data.get('phone', None)
        password = data.get('password', None)

        if not phone or not password:
            raise serializers.ValidationError('phone and password are required.')

        user = User.objects.filter(phone=phone).first()
        if user:
            if check_password(password, user.password):
                return user 
            else:
                raise serializers.ValidationError('Invalid password.')
        else:
            raise serializers.ValidationError('User does not exist.')

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'phone']  

class UserAddressInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields = ['id', 'apartment_number', 'street', 'city', 'province', 'des']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not check_password(value, user.password):
            raise serializers.ValidationError('Incorrect old password.')
        return value

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'dob']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.save()
        return instance

class UpdateAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['apartment_number', 'street', 'city', 'province', 'des']

    def update(self, instance, validated_data):
        instance.apartment_number = validated_data.get('apartment_number', instance.apartment_number)
        instance.street = validated_data.get('street', instance.street)
        instance.city= validated_data.get('city', instance.city)
        instance.province = validated_data.get('province', instance.province)
        instance.des = validated_data.get('des', instance.des)
        instance.save()
        return instance