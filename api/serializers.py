from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import Anime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class AnimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['rating', 'name', 'genre']


class AnimesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['name', 'genre', 'episodes']


class CreateAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ["name", "genre", "type", "episodes", "rating", "members"]
