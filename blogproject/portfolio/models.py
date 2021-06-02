from django.db import models

# Create your models here.


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    images = models.ImageField(upload_to = 'images/',default='SOME STRING')
    description = models.CharField(max_length=100,default='SOME STRING')
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title
   