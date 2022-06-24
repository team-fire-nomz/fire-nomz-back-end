from dataclasses import fields
from rest_framework import serializers
from djoser.serializers import UserSerializer as DjoserUserSerializer
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from .models import RecipeVersion, Note, User, TasterFeedback


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

class RecipeVersionSerializer(serializers.ModelSerializer):
    chef        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    notes = serializers.SlugRelatedField(many=True, read_only=True, slug_field='note')

    class Meta:
        model  = RecipeVersion
        fields = [
            'id',
            'title',
            'version_number',
            'ingredients',
            'recipe_steps',
            'image',
            'ready_for_feedback',
            'successful_variation',
            'chef',
            'created_at',
            'notes',
            ]


class NoteSerializer(serializers.ModelSerializer):
    note_by        = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Note
        fields = [
            'id',
            'note',
            'note_by',
            'recipe_version',
            'created_at',
        ]

class TasterFeedbackSerializer(serializers.ModelSerializer):
    tester = serializers.SlugRelatedField(read_only=True, slug_field="username")
    # test_version_number = serializers.SlugRelatedField(read_only=True, slug_field="test_version_number")
    # rating = serializers.MultipleChoiceField(choices = TasterFeedback.RADIO)
    # saltiness = serializers.MultipleChoiceField(choices = TasterFeedback.SCALE)
    # sweetness = serializers.MultipleChoiceField(choices = TasterFeedback.SCALE)
    # portion = serializers.MultipleChoiceField(choices = TasterFeedback.SCALE)
    # texture = serializers.MultipleChoiceField(choices = TasterFeedback.CHOICE)


    class Meta:
        model = TasterFeedback
        fields = [
            'id',
            'created_at',
            # 'test_version_number',
            'tester',
            'rating',
            'saltiness',
            'sweetness',
            'portion',
            'texture',
            'additional_comment',
        ]


class TasterFeedbackDetailSerializer(serializers.ModelSerializer):
    tester = serializers.SlugRelatedField(read_only=True, slug_field="username")

    # rating = serializers.MultipleChoiceField(choices = TasterFeedback.RADIO)
    # saltiness = serializers.MultipleChoiceField(choices = TasterFeedback.SCALE)
    # sweetness = serializers.MultipleChoiceField(choices = TasterFeedback.SCALE)
    # portion = serializers.MultipleChoiceField(choices = TasterFeedback.SCALE)
    # texture = serializers.MultipleChoiceField(choices = TasterFeedback.CHOICE)


    class Meta:
        model = TasterFeedback
        fields = [
            'id',
            'test_recipe',
            'rating',
            'saltiness',
            'sweetness',
            'portion',
            'texture',
            'additional_comment',
            'tester',
            'created_at',
        ]