from django.db import models


# Create your models here.



class Post(models.Model):
    title = models.CharField(
        max_length=50,
        default="무제"
    )
    photo = models.ImageField(upload_to='post')
    content = models.TextField(
       blank=True,
       null=True,
    )
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

