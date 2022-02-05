from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('author' , 'title', 'pub_date')
    list_filter = ('title',)
    search_fields = ['author' , 'title']


admin.site.register(Post, PostAdmin)