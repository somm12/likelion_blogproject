from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(blank=True, null=True,max_length=200)
    writer = models.CharField(blank=True, null=True,max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField(blank=True, null=True)
     # 게시글 Post에 이미지 추가
    image = models.ImageField(upload_to ="blog/",blank=True, null=True)
    

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]