from django.db import models

# Create your models here.
from django.db import models

class Excuse(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return self.content
