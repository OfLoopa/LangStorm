from django.db import models


class Word(models.Model):
    english_writing = models.CharField(max_length=40)
    translation = models.CharField(max_length=40)

    transcription = models.CharField(max_length=50, null=True, blank=True)
    example = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.english_writing


class Lesson(models.Model):
    summary = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.summary[0:50]


class Dictionary(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.lesson)


class DictionaryRecord(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "dict id - " + str(self.dictionary) + "; word - " + str(self.word)
