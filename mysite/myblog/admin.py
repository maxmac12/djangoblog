from django.contrib import admin
from myblog.models import Post, Category

# Register your models here.


class CategoryInline(admin.StackedInline):
    model = Category.posts.through


#@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, ]
    date_hierarchy = 'created_date'


#@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
