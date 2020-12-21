from django.db import models

# Create your models here.
class Todo(models.Model):
  title = models.CharField('タイトル', max_length = 100)
  deadline = models.DateField('期限')
  
  def __str__(self):
    return self.title