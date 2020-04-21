from django.db import models

class Question(models.Model):
  text = models.CharField(max_length = 200)
  publish_date = models.DateTimeField('Date published')

  def __str__(self):
    return self.text

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choise_text = models.CharField(max_length = 200)
  votes = models.IntegerField(default = 0)

  def __str__(self):
    return self.choise_text
