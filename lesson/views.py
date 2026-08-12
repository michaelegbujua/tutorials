from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lesson, category
from .serializers import LessonSerializer

class ViewLesson(APIView):
    def get(self, request):
        lessons = Lesson.objects.all().select_related('category')
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateLesson(APIView):
    def post(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)