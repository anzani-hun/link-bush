from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MyLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    visible = models.BooleanField(default = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.title