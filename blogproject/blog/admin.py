from django.contrib import admin
from .models import Post,Tag,Category

# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
