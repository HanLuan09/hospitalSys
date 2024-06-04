from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user_service.authentication import SafeJWTAuthentication
from user_service.utils import generate_access_token, generate_refresh_token
from user_service.models import UserProfile, Role
from .serializers import  UserInfoSerializer, UserSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            user_role, _ = Role.objects.get_or_create(name='USER')
            user.roles.add(user_role)

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
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyTokenView(APIView):
    authentication_classes = [SafeJWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({'message': 'Token is valid.'}, status=status.HTTP_200_OK)

class ValidTokenView(APIView):
    authentication_classes = [SafeJWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        return Response({'valid': True}, status=status.HTTP_200_OK)