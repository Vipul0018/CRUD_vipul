from django.contrib import admin
from .models import Blog,Likes
# Register your models here.
@admin.register(Likes)
class AdminBlog(admin.ModelAdmin):
     list_display = ['id','Owner_ID','like']
@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
     list_display = ['id','Owner_ID','Title','Content','is_public','like']