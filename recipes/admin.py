from django.contrib import admin
from .models import Recipe, Tag, Ingredient, Ingredients_recipe, Follow, Favorite


class Ingredients_recipeInline(admin.TabularInline):
    model = Ingredients_recipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("pk", 'title', 'cooking_time', 'text', 'author', 'pub_date') 
    empty_value_display = '-пусто-'
    inlines = (Ingredients_recipeInline,)


class TagAdmin(admin.ModelAdmin):
    list_display = ("pk", 'title', 'color_tags', 'style') 
    empty_value_display = '-пусто-'


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", 'title', 'dimension') 
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = ("pk", 'user', 'author') 
    empty_value_display = '-пусто-'


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("pk", 'user', 'recipe') 
    empty_value_display = '-пусто-'


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Favorite, FavoriteAdmin)

