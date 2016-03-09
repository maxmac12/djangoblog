from django.contrib import admin

from .models import Post, Category


class CategoryInline(admin.StackedInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    exclude =('posts',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'modified_date', 'author')
    inlines = [CategoryInline,]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)


