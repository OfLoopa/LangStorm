from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import (
    getWordsList, createWord, getWordCard,
    updateWord, deleteWord, getLessonsList,
    createLesson, getLessonDetail, updateLesson, deleteLesson
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
            'body': {'body': ''},
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
            'body': {'body': ''},
            'description': 'Update information in a word\'s card',
        },
        {
            'Endpoint': '/words/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete card with a word',
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
            'body': {'body': ''},
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
            'method': 'PUT',
            'body': {'body': ''},
            'description': 'Update information in a lesson\'s card',
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
        return getWordsList(request)

    if request.method == 'POST':
        return createWord(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getWord(request, pk):

    if request.method == 'GET':
        return getWordCard(request, pk)

    if request.method == 'PUT':
        return updateWord(request, pk)

    if request.method == 'DELETE':
        return deleteWord(request, pk)


@api_view(['GET', 'POST'])
def getLessons(request):

    if request.method == 'GET':
        return getLessonsList(request)

    if request.method == 'POST':
        return createLesson(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getLesson(request, pk):

    if request.method == 'GET':
        return getLessonDetail(request, pk)

    if request.method == 'PUT':
        return updateLesson(request, pk)

    if request.method == 'DELETE':
        return deleteLesson(request, pk)
