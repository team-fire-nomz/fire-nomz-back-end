from django.contrib import admin
from .models import User, Test, Recipe, TasterFeedback

admin.site.register(User)
admin.site.register(Test)
admin.site.register(Recipe)
admin.site.register(TasterFeedback)
