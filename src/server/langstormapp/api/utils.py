from rest_framework.response import Response
from .models import Word, DictionaryRecord, Lesson
from .serializer import WordSerializer, DictionaryRecordSerializer, LessonSerializer


def getWordsList(request):
    words = Word.objects.all()
    serializer = WordSerializer(words, many=True)
    return Response(serializer.data)


def createWord(request):
    data = request.data
    word = Word.objects.create(
        body=data['body']
    )
    serializer = WordSerializer(word, many=False)
    return Response(serializer.data)


def getWordCard(request, pk):
    word = Word.objects.get(id=pk)
    serializer = WordSerializer(word, many=False)
    return Response(serializer.data)


def updateWord(request, pk):
    data = request.data
    word = Word.objects.get(id=pk)
    serializer = WordSerializer(instance=word, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteWord(request, pk):
    word = Word.objects.get(id=pk)
    word.delete()
    return Response('Word was deleted!')


def getLessonsList(request):
    lessons = Lesson.objects.all()
    serializer = WordSerializer(lessons, many=True)
    return Response(serializer.data)


def createLesson(request, pk):
    pass


def getLessonDetail(request):
    pass


def updateLesson(request, pk):
    pass


def deleteLesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    lesson.delete()
    return Response('Lesson was deleted!')
