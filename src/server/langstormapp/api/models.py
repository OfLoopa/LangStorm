from django.db import models


class Word(models.Model):
    english_writing = models.CharField(max_length=40)
    translation = models.CharField(max_length=40)

    transcription = models.CharField(max_length=50)
    example = models.CharField(max_length=300)

    def __str__(self):
        return self.english_writing


class DictionaryRecord(models.Model):
    dictionary_id = models.IntegerField()
    word = models.ForeignObject(Word, on_delete=models.CASCADE)

    def __str__(self):
        return self.word + self.dictionary_id


class Lesson(models.Model):
    summary = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    lesson_dict_id = models.IntegerField()

    def __str__(self):
        return self.summary[0:50]

