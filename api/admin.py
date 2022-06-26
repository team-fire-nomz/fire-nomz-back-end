from django.contrib import admin
from .models import User, RecipeVersion, Note, Ingredient, TasterFeedback

admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(Note)
admin.site.register(TasterFeedback)

@admin.register(RecipeVersion)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'chef', 'tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
