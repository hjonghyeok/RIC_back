from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=200) # title 컬럼
    content = models.TextField()             # content 컬럼
    views = models.FloatField(default=0)   # views 컬럼
    date = models.DateTimeField(auto_now_add=True, null=True) # data 컬럼

    def __str__(self):
        """A string representation of the model."""
        return self.title