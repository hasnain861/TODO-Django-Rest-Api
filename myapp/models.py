from django.db import models

# Create your models here.


class Task(models.Model):
    name        = models.TextField(max_length=100)
    created_on  = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

 
