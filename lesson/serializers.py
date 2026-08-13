from rest_framework import serializers
from .models import Tag, category, Lesson

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']  # Include only the 'id' and 'name' fields in the serialized output

class LessonSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)  # Serialize the related tags

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'category', 'tags', 'description', 'created_at', 'updated_at']