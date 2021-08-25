from django.db import models
from django.urls import reverse 

   
class Questions(models.Model):
    question = models.CharField(max_length = 200)
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.question

    def get_absolute_url(self):         
        return reverse('question_detail', args=[str(self.id)])

# class Answers(models.Model):
#     text_questions = models.TextField(max_length=500)
#     multiplechoice = models.CharField(max_length=50)
#     ans_qus = models.ManyToManyField(Questions, related_name='qustion_choice')
