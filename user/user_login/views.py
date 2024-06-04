from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user_service.models import UserProfile
from user_service.utils import generate_access_token, generate_refresh_token
from user_service.serializers import ChangePasswordSerializer, UserInfoSerializer, UserLoginSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data  
            access_token = generate_access_token(user)
            refresh_token = generate_refresh_token(user)

            user_serializer = UserInfoSerializer(user)

            user_profile = UserProfile.objects.filter(is_active=True, user=user).first()
            if user_profile:
                profile_serializer= UserProfileSerializer(user_profile).data
            else:
                profile_serializer = None

            return Response({
                'user': user_serializer.data,
                'profile': profile_serializer,
                'refresh': refresh_token,
                'access': access_token,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)