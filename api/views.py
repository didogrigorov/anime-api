from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Anime
from api.serializers import UserSerializer, AnimesSerializer, AnimesDataSerializer, CreateAnimeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ListAnimes(ListAPIView):
    queryset = Anime.objects.order_by("-rating").values()
    serializer_class = AnimesSerializer

class UpdateAPIView_Custom(mixins.UpdateModelMixin):
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
class AnimeName(RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimesDataSerializer
    lookup_field = 'name'

class ListCreateAnime(ListCreateAPIView):
    serializer_class = CreateAnimeSerializer
    queryset = Anime.objects.all()
    permission_classes = [IsAuthenticated]

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })