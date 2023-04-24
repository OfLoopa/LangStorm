from rest_framework.response import Response
from .models import Word, Dictionary, DictionaryRecord, Lesson
from .serializer import WordSerializer, DictionarySerializer, DictionaryRecordSerializer, LessonSerializer


# Words

def getWordsList():
    words = Word.objects.all()
    serializer = WordSerializer(words, many=True)
    return Response(serializer.data)


def createWord(request):
    data = request.data
    word = Word.objects.create(
        english_writing=data['english_writing'],
        translation=data["translation"],
        transcription=data["transcription"],
        example=data["example"]
    )
    serializer = WordSerializer(word, many=False)
    return Response(serializer.data)


def getWordCard(pk):
    word = Word.objects.get(id=pk)
    serializer = WordSerializer(word, many=False)
    return Response(serializer.data)


def updateWord(request, pk):
    data = request.data
    word = Word.objects.get(id=pk)
    serializer = WordSerializer(instance=word, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


def deleteWord(pk):
    word = Word.objects.get(id=pk)
    word.delete()
    return Response('Word was deleted!')


# Dictionary (Inner Instance)

def getDictionariesList():
    dictionaries = Dictionary.objects.all()
    return dictionaries


def createDictionary(lesson: Lesson | None, words: dict | None):
    if lesson is not None:
        dictionary = Dictionary.objects.create(
            lesson=lesson
        )
    else:
        dictionary = Dictionary.objects.create(
            lesson=""
        )

    if words is not None:
        for word in words:
            word = Word.objects.create(
                english_writing=word['english_writing'],
                translation=word["translation"],
                transcription=word["transcription"],
                example=word["example"]
            )
            dict_record = DictionaryRecord.objects.create(
                dictionary=dictionary,
                word=word
            )

    dict_records = list(
            DictionaryRecord.objects.all().filter(dictionary=dictionary)
        )

    return dictionary, dict_records


def getDictionary(pk):
    dictionary = Dictionary.objects.get(id=pk)
    dict_words = [
        WordSerializer(
            lesson_word.word, many=False
        ).data for lesson_word in list(
            DictionaryRecord.objects.all().filter(dictionary=dictionary)
        )
    ]

    dict_serializer = DictionarySerializer(dictionary, many=False)

    return


def addWordToDictionary(dictionary: Dictionary, word: dict):
    word = Word.objects.create(
        english_writing=word['english_writing'],
        translation=word["translation"],
        transcription=word["transcription"],
        example=word["example"]
    )
    dict_word = DictionaryRecord.objects.create(
        dictionary=dictionary,
        word=word
    )

    return Response(DictionaryRecordSerializer(dict_word, many=False).data)


def deleteWordDictionary(pk):
    word = Word.objects.get(id=pk)
    dict_word = DictionaryRecord.objects.get(word=word)
    dict_word.delete()
    return Response('Word from dictionary was deleted!')


def deleteDictionary(pk):
    dictionary = Dictionary.objects.get(id=pk)
    dictionary_records = DictionaryRecord.objects.all().filter(dictionary=dictionary)
    for record in dictionary_records:
        record.delete()
    dictionary.delete()
    return Response('Dictionary was deleted!')


# Lessons

def getLessonsList():
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)


def createLesson(request):
    data = request.data
    lesson = Lesson.objects.create(
        summary=data["lesson"]["summary"]
    )
    if 'words' in data.keys():
        createDictionary(lesson, data["words"])
    else:
        createDictionary(lesson, None)

    serializer = LessonSerializer(lesson, many=False)
    return Response(serializer.data)


def getLessonDetail(request, pk):
    lesson = Lesson.objects.get(id=pk)
    lesson_serializer = LessonSerializer(lesson, many=False)

    lesson_dict = [
        WordSerializer(
            lesson_word.word, many=False
        ).data for lesson_word in list(
            Dictionary.objects.all().filter(lesson=lesson)
        )
    ]

    return Response({"lesson": lesson_serializer.data, "words": lesson_dict})


def updateLesson(request, pk):
    data = request.data
    lesson = Lesson.objects.get(id=pk)
    lesson_serializer = WordSerializer(instance=lesson, data=data["lesson"])

    if lesson_serializer.is_valid():
        lesson_serializer.save()

    return Response({"lesson": lesson_serializer.data, "words": lesson_dict})


def deleteLesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    lesson.delete()
    return Response('Lesson was deleted!')
