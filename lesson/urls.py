from django.urls import path
from .views import ViewLesson, CreateLesson, ViewCategory

urlpatterns = [
    path('lessons/', ViewLesson.as_view(), name='lesson-list'),
    path('lessons/create/', CreateLesson.as_view(), name='lesson-create'),
    path('categories/', ViewCategory.as_view(), name='category-list'),
]