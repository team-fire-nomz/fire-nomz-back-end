from dataclasses import fields
from rest_framework import serializers
from djoser.serializers import UserSerializer as DjoserUserSerializer
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from .models import RecipeVersion, Note, User, TasterFeedback
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)

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


class RecipeVersionSerializer (serializers.ModelSerializer):
    chef        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    notes = serializers.SlugRelatedField(many=True, read_only=True, slug_field='note') #this is needed or notes is required during a POST
    ingredients = serializers.JSONField()
    recipe_steps =serializers.JSONField() # test tomorrow!!
    
    class Meta: 
        model  = RecipeVersion
        fields = [
            'id',
            'title',
            # 'version_number',
            'ingredients',
            'recipe_steps',
            'image',
            'ready_for_feedback',
            'successful_variation',
            'chef',
            'created_at',
            'notes',
            ]


class RecipeVersionDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    chef        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    notes = serializers.SlugRelatedField(many=True, read_only=True, slug_field='note') # this would show title.. so don't need -> may need as it's required if commented out
    # taster_feedbacks = serializers.SlugRelatedField(many=True, read_only=True, slug_field='test_recipe') -> can't serialize data
    ingredients = serializers.JSONField()
    recipe_steps =serializers.JSONField()
    tags = TagListSerializerField()

    class Meta:
        model  = RecipeVersion
        fields = [
            'id',
            'title',
            # 'version_number',
            'ingredients',
            'recipe_steps',
            'image',
            'ready_for_feedback',
            'successful_variation',
            'chef',
            'created_at',
            'notes',
            'taster_feedbacks',
            'tags',
            ]


#for taggit
class RecipeListSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = RecipeVersion
        fields = (
            'id',
            'title',
            'chef',
            'tags',
        )


class NoteSerializer(serializers.ModelSerializer):
    note_by        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    
    class Meta:
        model = Note
        fields = [
            'id',
            'note',
            'note_by',
            'created_at',
        ]


class NoteDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    note_by        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    tags = TagListSerializerField()

    class Meta:
        model = Note
        fields = [
            'id',
            'note',
            'note_by',
            'recipe_version',
            'tags',
            'created_at',
        ]


class TasterFeedbackSerializer(TaggitSerializer, serializers.ModelSerializer):
    # taster_id = serializers.SlugRelatedField(read_only=True, allow_null=True, slug_field="username")

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
            # 'taster',
            'rating',
            'saltiness',
            'sweetness',
            'portion',
            'texture',
            'additional_comment',
        ]


class TasterFeedbackDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    # taster_id = serializers.SlugRelatedField(read_only=True, allow_null=True, slug_field="username")
    # test_recipe = serializers.PrimaryKeyRelatedField(read_only=True)
    
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
            # 'taster',
            'test_recipe', # PK of RecipeVversion
            'rating',
            'saltiness',
            'sweetness',
            'portion',
            'texture',
            'additional_comment',
        ]