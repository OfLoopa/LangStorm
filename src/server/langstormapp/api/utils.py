from django.db.models import QuerySet

from .models import Word, Dictionary, DictionaryRecord, Lesson
from .serializer import WordSerializer, DictionarySerializer, DictionaryRecordSerializer, LessonSerializer


# Word
def getWordsList() -> QuerySet:
    """
    Get all words

    :return: QuerySet
    """
    words = Word.objects.all()
    return words


def createWord(word: dict) -> QuerySet:
    """
    Write new word into db

    :param word: dict with structure
    {
        "english_writing": "",
        "translation": "",
        "transcription": "",
        "example": ""
    }
    :return: QuerySet
    """
    new_word = Word.objects.create(
        english_writing=word['english_writing'],
        translation=word["translation"],
        transcription=word["transcription"],
        example=word["example"]
    )
    return new_word


def getWordCard(pk: int) -> QuerySet:
    """
    Get word from database by its id

    :param pk: word's primary key
    :return: QuerySet
    """
    word = Word.objects.get(id=pk)
    return word


def updateWord(new_word: dict, pk: int) -> QuerySet:
    """
    Update word with given id

    :param new_word: dict with structure
    {
        "english_writing": "",
        "translation": "",
        "transcription": "",
        "example": ""
    }
    :param pk: word's primary key
    :return: QuerySet
    """
    word = Word.objects.get(id=pk)
    serializer = WordSerializer(instance=word, data=new_word)

    if serializer.is_valid():
        serializer.save()

    return Word.objects.get(id=pk)


def deleteWord(pk: int) -> None:
    """
    Delete word by id

    :param pk: word's primary key
    """
    word = Word.objects.get(id=pk)
    word.delete()


# Dictionary

def getDictionariesList() -> QuerySet:
    """
    Get list of all dictionaries

    :return: QuerySet
    """
    dictionaries = Dictionary.objects.all()
    return dictionaries


def getDictionaryInstance(pk: int) -> QuerySet:
    """
    Get Dictionary model object by id

    :param pk: dictionary's primary key
    :return: QuerySet
    """
    dictionary = Dictionary.objects.get(id=pk)
    return dictionary


def createDictionary(lesson: Lesson | None = None) -> QuerySet:
    """
    Create a new empty dictionary. Can be bind initially to a lesson

    :param lesson: Lesson model object
    :return: QuerySet
    """
    if lesson is not None:
        dictionary = Dictionary.objects.create(
            lesson=lesson
        )
    else:
        dictionary = Dictionary.objects.create()

    return dictionary


def bindDictionary(dictionary: Dictionary, lesson: Lesson) -> QuerySet:
    """
    Bind dictionary to given lesson

    :param dictionary: Dictionary model object
    :param lesson: Lesson object model
    :return: QuerySet
    """
    serializer = DictionarySerializer(instance=dictionary, data={"lesson": lesson})

    if serializer.is_valid():
        serializer.save()

    return getDictionaryInstance(dictionary.id)


def getDictionary(pk: int) -> dict[str, dict | list]:
    """
    Get dictionary with it id and list of words in it

    :param pk:
    :return: JSON-like object
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
    dictionary = Dictionary.objects.get(id=pk)
    dict_words = [
        WordSerializer(Word.objects.get(
            id=word_record.word_id
        ), many=False).data for word_record in list(
            DictionaryRecord.objects.all().filter(
                dictionary=dictionary
            )
        )
    ]

    return {"dict_info": DictionarySerializer(dictionary, many=False).data, "words": dict_words}


def addWordToDictionary(new_word: dict, dict_pk: int) -> QuerySet:
    """
    Add new word to word's cards and dictionary with given id

    :param new_word: dict with structure
    {
        "english_writing": "",
        "translation": "",
        "transcription": "",
        "example": ""
    }
    :param dict_pk: dictionary's primary key
    :return: QuerySet with record in dictionary
    """
    dictionary = Dictionary.objects.get(id=dict_pk)
    word = Word.objects.create(
        english_writing=new_word['english_writing'],
        translation=new_word["translation"],
        transcription=new_word["transcription"],
        example=new_word["example"]
    )
    dict_word = DictionaryRecord.objects.create(
        dictionary=dictionary,
        word=word
    )

    return dict_word


def deleteWordFromDictionary(dict_pk: int, word_pk: int) -> None:
    """
    Delete word with given id from dictionary

    :param dict_pk: dictionary's primary key
    :param word_pk: word's primary key
    """
    word = Word.objects.get(id=word_pk)
    dictionary = Dictionary.objects.get(id=dict_pk)
    dict_word = DictionaryRecord.objects.get(word=word, dictionary=dictionary)
    dict_word.delete()

    # delete empty dictionary:

    # dict_records = list(DictionaryRecord.objects.all().filter(dictionary=dictionary))
    # if len(dict_records) == 0:
    #     dictionary.delete()


def deleteDictionary(pk: int) -> None:
    """
    Delete dictionary

    :param pk: dictionary's primary key
    """
    dictionary = Dictionary.objects.get(id=pk)
    dictionary_records = DictionaryRecord.objects.all().filter(dictionary=dictionary)
    for record in dictionary_records:
        record.delete()
    dictionary.delete()


# Lessons

def getLessonsList() -> QuerySet:
    """
    Get list of lessons

    :return: QuerySet
    """
    lessons = Lesson.objects.all()
    return lessons


def getLessonInstance(pk: int) -> QuerySet:
    """
    Get Lesson model object by id

    :param pk: lesson's primary key
    :return: QuerySet
    """
    lesson = Lesson.objects.all().filter(id=pk)
    return lesson


def createLesson(summary: str, dictionary: Dictionary | None = None) -> QuerySet:
    """
    Create new lesson, optional with dictionary

    :param summary: lesson's summary
    :param dictionary: lesson's dictionary, default to None
    :return: QuerySet
    """
    lesson = Lesson.objects.create(
        summary=summary
    )
    if dictionary is not None:
        bindDictionary(dictionary, lesson)

    return lesson


def getLesson(pk: int) -> dict[str, dict]:
    """
    Get Lesson JSON with info and dictionary

    :param pk: lesson's primary key
    :return: JSON-like object
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
    lesson = getLessonInstance(pk)

    dictionary = Dictionary.objects.get(lesson=lesson)
    lesson_dict = getDictionary(dictionary.id)

    return {"lesson": LessonSerializer(lesson, many=False).data, "dictionary": lesson_dict}


def deleteLesson(pk: int) -> None:
    """
    Delete lesson by id with dictionary

    :param pk: lesson's primary key
    """
    lesson = Lesson.objects.get(id=pk)
    dictionary = Dictionary.objects.get(lesson=lesson)
    deleteDictionary(dictionary.id)
    lesson.delete()
