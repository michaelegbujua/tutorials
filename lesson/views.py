from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Lesson, category
from .serializers import CategorySerializer, LessonSerializer

class ViewLesson(APIView):
    def get(self, request):
        #selectrelated for foreignkey (category ), prefetch_related for ManyToMany (tags)
        lessons = Lesson.objects.all().select_related('category').prefetch_related('tags')
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#APIViews
class CreateLesson(APIView):
    def post(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Standard ListAPIView handles the get method automatically (generics.ListAPIView)
class ViewCategory(generics.ListAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

