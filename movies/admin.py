from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Movie, List, Category

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["email", "username",]

admin.site.register(User, CustomUserAdmin)
admin.site.register(Movie)
admin.site.register(List)
admin.site.register(Category)
