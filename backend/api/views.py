from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import RegisterSerializer, CharInventorySerializer
from .models import CharInventory
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

class CharInventoryPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'pageSize'
    max_page_size = 100

class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.validated_data["username"])
            tokens = get_tokens_for_user(user)
            return Response(tokens, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh)
    }

class CharInventoryView(viewsets.ModelViewSet):
    serializer_class = CharInventorySerializer
    queryset = CharInventory.objects.all()
    pagination_class = CharInventoryPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params

        item_name = params.get('itemName')
        char_name = params.get('charName')

        if item_name:
            queryset = queryset.filter(item_name__icontains=item_name)
        if char_name:
            queryset = queryset.filter(char_name__icontains=char_name)

        return queryset

class CharNamesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        char_names = CharInventory.objects.values('char_name').distinct()
        charname_list = [entry['char_name'] for entry in char_names]
        return Response(charname_list)



