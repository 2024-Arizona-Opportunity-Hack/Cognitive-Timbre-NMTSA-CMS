from django.db import models

class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name + " (" + self.url + ")" 