from rest_framework import serializers
from .models import Tag, category, Lesson, Question, Option

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']  # Include only the 'name' fields in the serialized output

class LessonSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)  # Serialize the related tags

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'category', 'tags', 'description', 'created_at', 'updated_at']


#quiz selializers

#Option
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, required=False)  # Serialize the related options

    class Meta:
        model = Question
        fields = ['id', 'lesson', 'text', 'options', 'created_at', 'updated_at']

    def create(self, validated_data):
        options_data = validated_data.pop('options', [])
        question = Question.objects.create(**validated_data)
        for option_data in options_data:
            Option.objects.create(question=question, **option_data)
        return question
