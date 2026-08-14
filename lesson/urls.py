from django.urls import path
from .views import ViewLesson, CreateLesson, ViewCategory, QuestionListCreateAPIView, LessonQuizAPIView 




urlpatterns = [
    #category endpoint
    path('categories/', ViewCategory.as_view(), name='category-list'),

    #lesson  endpoints
    path('lessons/', ViewLesson.as_view(), name='lesson-list'),
    path('lessons/create/', CreateLesson.as_view(), name='lesson-create'),

    #Quiz endpoints
    path('questions/', QuestionListCreateAPIView.as_view(), name='question-list-create'),
    path('lessons/<int:lesson_id>/questions/', LessonQuizAPIView.as_view(), name='lesson-quiz'),
]



                        