from django.contrib import admin
from .models import User, Note, RecipeVersion, TasterFeedback

admin.site.register(User)
admin.site.register(Note)
admin.site.register(RecipeVersion)
admin.site.register(TasterFeedback)
