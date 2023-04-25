from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils_api import (
    getWordsListAPI, createWordAPI, getWordCardAPI,
    updateWordAPI, deleteWordAPI, getDictionariesListAPI, createDictionaryAPI,
    getDictionaryAPI, addWordToDictionaryAPI, deleteWordFromDictionaryAPI,
    bindDictionaryAPI, deleteDictionaryAPI,
    getLessonsListAPI, createLessonAPI, getLessonAPI, deleteLessonAPI
)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/words/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of all words with translation and other details that was added',
        },
        {
            'Endpoint': '/words/',
            'method': 'POST',
            'body': {
                'english_writing': '',
                'translation': '',
                'transcription': '',
                'example': '',
            },
            'description': 'Create a new word card',
        },
        {
            'Endpoint': '/words/id',
            'method': 'GET',
            'body': None,
            'description': 'Get a card with word, translation and other details',
        },
        {
            'Endpoint': '/words/id',
            'method': 'PUT',
            'body': {
                'english_writing': '',
                'translation': '',
                'transcription': '',
                'example': '',
            },
            'description': 'Update information in a word\'s card',
        },
        {
            'Endpoint': '/words/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete card with a word',
        },

        {
            'Endpoint': '/dictionaries/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of all dictionary instances',
        },
        {
            'Endpoint': '/dictionaries/',
            'method': 'POST',
            'body': {'lesson_id': ''},
            'description': 'Create empty dictionary. If body is not empty - bind it to lesson by id',
        },
        {
            'Endpoint': '/dictionaries/id',
            'method': 'GET',
            'body': None,
            'description': 'Get dictionary with words',
        },
        {
            'Endpoint': '/dictionaries/id',
            'method': 'PUT',
            'body': {
                'add word': {
                    'word': {
                        'english_writing': '',
                        'translation': '',
                        'transcription': '',
                        'example': '',
                    }
                },
                'delete word': {
                    'word_id': ''
                },
                'bind lesson': {
                    'lesson_id': '',
                }
            },
            'description': 'Update dictionary. '
                           'To add words use body "Add word". '
                           'To delete word use body "Delete word".'
                           'To bind lesson to dictionary use body "Bind lesson"',
        },
        {
            'Endpoint': '/dictionaries/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete dictionary',
        },

        {
            'Endpoint': '/lessons/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of all lessons',
        },
        {
            'Endpoint': '/lessons/',
            'method': 'POST',
            'body': {
                'summary': '',
                'dict_id': ''
            },
            'description': 'Create a new lesson record',
        },
        {
            'Endpoint': '/lessons/id',
            'method': 'GET',
            'body': None,
            'description': 'Get a lesson info with date, summary and words',
        },
        {
            'Endpoint': '/lessons/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete card with a lesson',
        },
    ]

    return Response(routes)


@api_view(['GET', 'POST'])
def getWords(request):

    if request.method == 'GET':
        return getWordsListAPI()

    if request.method == 'POST':
        return createWordAPI(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getWord(request, pk):

    if request.method == 'GET':
        return getWordCardAPI(pk)

    if request.method == 'PUT':
        return updateWordAPI(request, pk)

    if request.method == 'DELETE':
        return deleteWordAPI(pk)


@api_view(['GET', 'POST'])
def getDictionaries(request):

    if request.method == 'GET':
        return getDictionariesListAPI()

    if request.method == 'POST':
        return createDictionaryAPI(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getDictionary(request, pk):

    if request.method == 'GET':
        return getDictionaryAPI(pk)

    if request.method == 'PUT':
        if 'word' in request.data.keys():
            return addWordToDictionaryAPI(request, pk)
        elif 'word_id' in request.data.keys():
            return deleteWordFromDictionaryAPI(request, pk)
        elif 'lesson_id' in request.data.keys():
            return bindDictionaryAPI(request, pk)

    if request.method == 'DELETE':
        return deleteDictionaryAPI(pk)


@api_view(['GET', 'POST'])
def getLessons(request):

    if request.method == 'GET':
        return getLessonsListAPI()

    if request.method == 'POST':
        return createLessonAPI(request)


@api_view(['GET', 'DELETE'])
def getLesson(request, pk):

    if request.method == 'GET':
        return getLessonAPI(pk)

    if request.method == 'DELETE':
        return deleteLessonAPI(pk)
