from django.contrib import admin
from .models import Post


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'Description', 'status', 'created_on')
#     list_filter = ("status",)
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'Description': ('title',)}


admin.site.register(Post)