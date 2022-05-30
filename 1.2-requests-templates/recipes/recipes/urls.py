from django.contrib import admin
from django.urls import path

from calculator.views import calculate_recipe_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('<recipe_name>/', calculate_recipe_view, name='calculate_recipe')
]