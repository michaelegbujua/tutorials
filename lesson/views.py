from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Lesson, category, Question
from .serializers import CategorySerializer, LessonSerializer, QuestionSerializer, OptionSerializer







# Standard ListAPIView handles the get method automatically (generics.ListAPIView)
class ViewCategory(generics.ListAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

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


#Quiz view (using the APIView class)
class QuestionListCreateAPIView(APIView):
    """
    GET: List all questions across all lessons.
    POST: Create a new question with its options.
    """
    def get(self, request):
        questions = Question.objects.all().select_related('lesson').prefetch_related('options')
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonQuizAPIView(APIView):
    """
    GET: Fetch all questions for a specific lesson by lesson_id
    """
    def get(self, request, lesson_id):
        questions = Question.objects.filter(lesson_id=lesson_id).prefetch_related('options')
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)