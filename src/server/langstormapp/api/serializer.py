from rest_framework.serializers import ModelSerializer
from .models import Word, Dictionary, DictionaryRecord, Lesson


class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class DictionarySerializer(ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'


class DictionaryRecordSerializer(ModelSerializer):
    class Meta:
        model = DictionaryRecord
        fields = '__all__'
