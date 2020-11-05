from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_recipe, name='recipe_new'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/<int:recipe_id>/', views.recipe, name='recipe'),
    path('<username>/<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('<username>/<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),
]
