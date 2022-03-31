from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Movie, List, Category, Friend


admin.site.register(User)
admin.site.register(Movie)
admin.site.register(List)
admin.site.register(Category)