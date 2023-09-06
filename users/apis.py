from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import CreateUserSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken


class CreateUserView(APIView):
    
    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        # print(serializer.is_valid())
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            refresh = RefreshToken.for_user(user)
            
            user_data = UserSerializer(user).data

            ret_value =  {
                **user_data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        
            return Response(ret_value, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    pass
