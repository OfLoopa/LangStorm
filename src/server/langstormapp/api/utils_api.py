from rest_framework.response import Response
from .models import Word, Dictionary, DictionaryRecord, Lesson
from .serializer import WordSerializer, DictionarySerializer, DictionaryRecordSerializer, LessonSerializer
from .utils import (
    getWordsList, createWord, getWordCard, updateWord, deleteWord,
    getDictionariesList, getDictionaryInstance, createDictionary,
    bindDictionary, getDictionary, addWordToDictionary,
    deleteWordFromDictionary, deleteDictionary,
    getLessonsList, getLessonInstance, createLesson,
    getLesson, deleteLesson
)


# ___________ Words API ______________________________

def getWordsListAPI():
    """
    Get list of words

    :return: JSON object
    """
    words = getWordsList()
    serializer = WordSerializer(words, many=True)
    return Response(serializer.data)


def createWordAPI(request):
    """
    Write new word

    :param request: POST-request with body
    {"english_writing": "",
    "translation": "",
    "transcription": "",
    "example": ""}
    :return: HTTP-response with word's JSON
    """
    word = request.data
    new_word = createWord(word)
    serializer = WordSerializer(new_word, many=False)
    return Response(serializer.data)


def getWordCardAPI(pk: int):
    """
    Get JSON with word card

    :param pk: word's primary key
    :return: HTTP-response with word's JSON
    """
    word = getWordCard(pk)
    serializer = WordSerializer(word, many=False)
    return Response(serializer.data)


def updateWordAPI(request, pk):
    """
    Update word's card

    :param request: POST-request with body
    {"english_writing": "",
    "translation": "",
    "transcription": "",
    "example": ""}
    :param pk: word's primary key
    :return: HTTP-response with word's JSON
    """
    data = request.data
    word = updateWord(data, pk)
    serializer = WordSerializer(word, many=False)

    return Response(serializer.data)


def deleteWordAPI(pk):
    """
    Delete word's card

    :param pk: word's primary key
    :return: HTTP-response
    """
    deleteWord(pk)
    return Response('Word was deleted!')


# ____________ Dictionary ____________________________

def getDictionariesListAPI():
    """
    Get list of dictionaries instances

    :return: HTTP-response with JSON
    """
    dictionaries = [DictionarySerializer(dictionary, many=False).data for dictionary in list(getDictionariesList())]
    return Response(dictionaries)


def createDictionaryAPI(request):
    """
    Create empty dictionary. Can be bind to existing lesson during initialize

    :param request:  POST-request with body
    {"lesson_id": 0} (Optional)
    :return: HTTP-response with dictionary instance in JSON
    """
    data = request.data
    lesson = getLesson(data['lesson_id']) if 'lesson_id' in data.keys() else None
    dictionary = createDictionary(lesson)

    return Response(DictionarySerializer(dictionary, many=False))


def getDictionaryAPI(pk: int):
    """
    Get full dictionary with words by id

    :param pk: dictionary's primary key
    :return: HTTP-Response with JSON object
    {
        "dict_info": {"id": 0, "lesson_id: ""};
        "words": [{
            "english_writing": "",
            "translation": "",
            "transcription": "",
            "example": ""
        }]
    }
    """
    dictionary = getDictionary(pk)
    return Response(dictionary)


def addWordToDictionaryAPI(request, pk):
    """
    Add word to a dictionary

    :param pk: dictionary primary key
    :param request: HTTP-PUT with JSON
    {
        "word": {
            "english_writing": "",
            "translation": "",
            "transcription": "",
            "example": ""
        }
    }
    :return: HTTP-response with dictionary record JSON
    """
    data = request.data
    dict_record = addWordToDictionary(data['word'], pk)

    return Response(DictionaryRecordSerializer(dict_record, many=False).data)


def deleteWordFromDictionaryAPI(request, pk):
    """
    Delete word with given id from dictionary

    :param pk: dictionary primary key
    :param request: HTTP-PUT with JSON
    {
        "word_id": ""
    }
    :return: HTTP-Response
    """
    data = request.data
    deleteWordFromDictionary(pk, data['word_id'])
    return Response('Word from dictionary was deleted!')


def bindDictionaryAPI(request, pk):
    """
    Bind given lesson to dictionary

    :param pk: dictionary primary key
    :param request: HTTP-PUT with JSON
    {
        "lesson_id": ""
    }
    :return: HTTP-Response with dictionary instance JSON
    """
    data = request.data
    dictionary = bindDictionary(pk, data['lesson_id'])

    return Response(DictionarySerializer(dictionary, many=False).data)


def deleteDictionaryAPI(pk):
    """
    Delete dictionary by id

    :param pk: dictionary's primary key
    :return: HTTP-Response
    """
    deleteDictionary(pk)
    return Response('Dictionary was deleted!')


# _________________ Lessons __________________________

def getLessonsListAPI():
    """
    Get list of lessons

    :return: HTTP-Response with JSON containing array of lesson instances
    """
    lessons = getLessonsList()
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)


def createLessonAPI(request):
    """
    Create a lesson card with given summary and dictionary

    :param request: HTTP-Post with JSON
    {
        'summary': '',
        'dict_id': 0
    }
    :return: HTTP-Response with lesson instance in JSON
    """
    data = request.data
    dictionary = getDictionaryInstance(data['dict_id'])
    lesson = createLesson(data['summary'], dictionary[0])

    lesson_serializer = LessonSerializer(lesson, many=False)
    return Response(lesson_serializer.data)


def getLessonAPI(pk):
    """
    Get card with lesson information (summary, dictionary)

    :param pk: lesson's primary key
    :return: HTTP-Response with JSON
    {"lesson":
        {"id": 0, "summary": ""},
    "dictionary":
        {"dict_info":
            {"id": 0, "lesson_id: ""},
        "words":
            [{"english_writing": "",
            "translation": "",
            "transcription": "",
            "example": ""}]
        }
    }
    """
    lesson = getLesson(pk)

    return Response(lesson)


def deleteLessonAPI(pk):
    """
    Delete lesson with given id

    :param pk: lesson's primary key
    :return: HTTP-Response
    """
    deleteLesson(pk)
    return Response('Lesson was deleted!')
