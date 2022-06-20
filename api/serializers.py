from dataclasses import fields
from rest_framework import serializers
from djoser.serializers import UserSerializer as DjoserUserSerializer
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from .models import Test, User, Recipe, TesterFeedback


class UserSerializer(DjoserUserSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'location',
            'business_name',
        )


class UserCreateSerializer(DjoserUserCreateSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'password',
            'last_name',
            'date_joined',
            'location',
            'business_name',
        )

class RecipeSerializer(serializers.ModelSerializer):
    chef        = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model  = Recipe
        fields = [
            'id',
            'title',
            'ingredients',
            'recipe',
            'chef',
            'created_at',
            ]


class TestSerializer(serializers.ModelSerializer):
    #might change to Name once User model is discussed futher
    chef        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    title       = serializers.SlugRelatedField(read_only=True, slug_field="title")
    class Meta:
        model  = Test
        fields = [
            'id',
            'title',
            'version_number',
            'ingredients',
            'recipe',
            'image',
            'outside_notes',
            'final_notes',
            'adjustments',
            'feedback_link',
            'tags',
            'chef',
            'variation_complete',
            'created_at',
            'successful_variation',
        ]

class FeedbackTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = TesterFeedback
        fields = [
            'rating',
            'saltiness',
            'sweetness',
            'portion',
            'texture',
            'additonal_comment',
            'created_at',
            'tester',
        ]