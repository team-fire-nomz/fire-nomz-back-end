from django.shortcuts import render
from djoser.views import UserViewSet as DjoserUserViewSet
from django.db.models import Count
from requests import Response
from rest_framework.generics import get_object_or_404, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from api.models import User, Recipe, RecipeVariation, Note, TasterFeedback
from rest_framework.viewsets import ModelViewSet
from api.serializers import NoteDetailSerializer, NoteSerializer, RecipeListSerializer, RecipeSerializer, TaggitRecipeListSerializer, RecipeVariationSerializer, RecipeVariationDetailSerializer, UserCreateSerializer, UserSerializer, TasterFeedbackSerializer, TasterFeedbackDetailSerializer, RecipeListDetailSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsChefOrReadOnly, RecipeIsChefOrReadOnly
from django.db.models import Q
from taggit.models import Tag
from django.db.models.query import QuerySet


class UserViewSet(DjoserUserViewSet):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            serializer_class = UserCreateSerializer
        else:
            serializer_class = UserSerializer
        return serializer_class


# For recipes-list/ & now recipes/
class RecipeListView(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
    permission_classes = (RecipeIsChefOrReadOnly,)

    def get_queryset(self):
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            results = Recipe.objects.filter(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term)
            )
            results

        else:
            results = Recipe.objects.all().order_by('-id')
        return results.order_by('-id')

    def perform_create(self, serializer):
        recipe_id = get_object_or_404(Recipe, pk=self.kwargs["recipe_pk"])
        serializer.save(chef=self.request.user, recipe_id=recipe_id)


# For recipes-list/ & now recipes/pk
class RecipeListDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListDetailSerializer
    permission_classes = (RecipeIsChefOrReadOnly,)

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
            if self.request.user.is_authenticated:
                queryset = queryset.filter(chef=self.request.user)
        return queryset.order_by('-id')


# For recipes/pk/recipe-variation
class RecipeVariationViewSet(ModelViewSet):
    queryset          = RecipeVariation.objects.all()
    serializer_class  = RecipeVariationSerializer
    permission_classes = (RecipeIsChefOrReadOnly,)

    # # for taggit - not sure if this is needed here
    def index(request):
        # recipe_versions =RecipeVariation.get.prefetch_related('tags').all()
        tags = Tag.objects.all()
        context = {'tags': tags} # removed 'recipe_versions':recipe_versions
        return render(request, 'api/index.html', context) # likely need to modify this as this is going to a page F/E isn't doing?!

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
            if self.request.user.is_authenticated:
                queryset = queryset.filter(chef=self.request.user)
        return queryset.annotate(
                total_answers=Count('notes')
            )

    def perform_create(self, serializer):
        serializer.save(chef=self.request.user)

    def perform_destroy(self, instance):
        if self.request.user  == instance.chef:
            instance.delete()

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.chef:
            serializer.save()

    def get_serializer_class(self):
        # Original working
        # if self.action in ['retrieve']:
        #     return RecipeVariationSerializer
        # return super().get_serializer_class()

        # Test separate serializers
        if self.request.method == 'POST':
            return RecipeVariationSerializer
        return RecipeVariationDetailSerializer


# For recipes/pk/new-variation/ -> shouldn't need since RecipeVariation should take it's place
class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer # do I use this one or create new?
    permission_classes = (RecipeIsChefOrReadOnly,) # or IsAuthenticatedOrReadOnly

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        # recipe_version = get_object_or_404(RecipeVariation, pk=self.kwargs["recipe_pk"])
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
            queryset = queryset.filter() # removed recipe_version=recipe_version

        return queryset.order_by('-id')

    def perform_create(self, serializer):
        serializer.save(chef=self.request.user)

    def perform_destroy(self, instance):
        if self.request.user  == instance.chef:
            instance.delete()

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.chef:
            serializer.save()


    # does this need to be specific?!
    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return RecipeViewSet
    #     return RecipeVariationDetailSerializer


# for all-recipes/ search
class AllRecipeVariationViewSet(ModelViewSet):
    queryset          = RecipeVariation.objects.all()
    serializer_class  = RecipeVariationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # for taggit - not sure if this is needed here
    def index(request):
        # recipe_versions =RecipeVariation.get.prefetch_related('tags').all()
        tags = Tag.objects.all()
        context = {'tags': tags} # removed 'recipe_versions':recipe_versions
        return render(request, 'api/index.html', context) # likely need to modify this as this is going to a page F/E isn't doing?!

    def get_queryset(self):
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            results = RecipeVariation.objects.filter(
                Q(title__icontains=search_term) |
                Q(ingredients__icontains=search_term)
            )
            results.order_by('-id')

        else:
            results = RecipeVariation.objects.annotate(
                total_recipes=Count('recipe_steps')
            )
        return results.order_by('-id')
    

# For recipes/pk/notes/
class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsChefOrReadOnly]

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        recipe_version = get_object_or_404(RecipeVariation, pk=self.kwargs["recipe_pk"])
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
            queryset = queryset.filter(recipe_version=recipe_version)

        return queryset

    def perform_create(self, serializer):
        recipe_version = get_object_or_404(RecipeVariation, pk=self.kwargs["recipe_pk"])
        if self.request.user.is_authenticated:
            serializer.save(note_by=self.request.user, recipe_version=recipe_version)

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.note_by:
            serializer.save()

    def get_serializer_class(self):
        # Test separate serializers
        if self.request.method == 'POST':
            return NoteSerializer
        return NoteDetailSerializer


# For all-notes/ search
class AllNoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            results = Note.objects.filter(
                Q(note__icontains=search_term)
                )
            results

        else:
            results = Note.objects.annotate(
                total_recipes=Count('note')
            )
        return results.order_by('-id')


class TasterFeedbackView(ModelViewSet):
    queryset = TasterFeedback.objects.all().order_by('created_at')
    serializer_class = TasterFeedbackSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            serializer_class = TasterFeedbackSerializer
        else:
            serializer_class = TasterFeedbackDetailSerializer
        return serializer_class

    def perform_create(self, serializer):
        test_recipe = get_object_or_404(RecipeVariation, pk=self.kwargs["recipe_pk"])
        if self.request.user.is_authenticated:
            serializer.save(tester=self.request.user, test_recipe=test_recipe)

    def perform_destroy(self, instance):
        if self.request.user  == instance.tester:
            instance.delete()

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.tester:
            serializer.save()


class TasterFeedbackDetailView(ModelViewSet):
    queryset = TasterFeedback.objects.all().order_by('created_at')
    serializer_class = TasterFeedbackDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        pass
        # assert self.queryset is not None, (
        #     "'%s' should either include a `queryset` attribute, "
        #     "or override the `get_queryset()` method."
        #     % self.__class__.__name__
        # )

        # queryset = self.queryset
        # if isinstance(queryset, QuerySet):
        #     # Ensure queryset is re-evaluated on each request.
        #     queryset = queryset.all()
        # return queryset

    def perform_destroy(self, instance):
        if self.request.user  == instance.tester:
            instance.delete()

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.tester:
            serializer.save()


# for Taggit
class RecipeListAPIView(ListAPIView):
    queryset = RecipeVariation.objects.all()
    serializer_class = TaggitRecipeListSerializer
