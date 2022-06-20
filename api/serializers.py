from dataclasses import fields
from tkinter import Scale
from rest_framework import serializers
from djoser.serializers import UserSerializer as DjoserUserSerializer
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from .models import Test, User, Recipe, TasterFeedback


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

# class FeedBackTest(object):
#     def __init__(self, saltiness, sweetness, portion, texture):
#         self.saltiness = saltiness
#         self.sweetness = sweetness
#         self.portion = portion
#         self.texture = texture

#     RADIO = ( 
#         ('ONE' , '1'), 
#         ('TWO' , '2'), 
#         ('THREE' , '3'), 
#         ('FOUR' , '4'), 
#         ('FIVE' , '5'), 
#     )

#     SCALE = ( 
#         ('TOO_LITTLE' , 'Too Little'), 
#         ('JUST_RIGHT' , 'Just Right'),
#         ('TOO_MUCH' , 'Too Much'), 
#     )

#     CHOICE = ( 
#         ('YES' , 'Yes'), 
#         ('NO' , 'No'), 
#     )



class TasterFeedbackSerializer(serializers.ModelSerializer):
    tester = serializers.SlugRelatedField(read_only=True, slug_field="username")

    rating = serializers.MultipleChoiceField(choices = TasterFeedback.RADIO)
    saltiness = serializers.MultipleChoiceField(choices = TasterFeedback.SCALE)
    sweetness = serializers.MultipleChoiceField(choices = TasterFeedback.SCALE)
    portion = serializers.MultipleChoiceField(choices = TasterFeedback.SCALE)
    texture = serializers.MultipleChoiceField(choices = TasterFeedback.CHOICE)


    class Meta:
        model = TasterFeedback
        fields = [
            'id',
            'version_number',
            'rating',
            'saltiness',
            'sweetness',
            'portion',
            'texture',
            'additional_comment',
            'created_at',
        ]