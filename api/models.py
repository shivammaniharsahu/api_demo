from django.db import models

# Create your models here.


class Basicinfo(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phoneno = models.PositiveIntegerField(default=1,unique=True)

    def __str__(self):
        return self.name
