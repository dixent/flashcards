from django.db import models
from django.core import validators

class Language(models.Model):
  name = models.CharField('Name', max_length = 50)
  code = models.CharField('Code', max_length = 3)

  def __str__(self):
    return self.name

class Card(models.Model):
  text = models.CharField('Text', max_length = 300)
  translation = models.CharField('Translation', max_length = 300)
  created_at = models.DateTimeField('Created at')
  learning_index = models.IntegerField(
    validators = [validators.MinValueValidator(0), validators.MaxValueValidator(10)]
  )
  language = models.ForeignKey(Language, on_delete = models.CASCADE)

  def __str__(self):
    return self.text
