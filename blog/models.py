from django.db import models
from django.utils import timezone

# below code line defines our model
class Post(models.Model):  #this means Post is a Django model and model in django is a special object inside a database
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def _str_(self):
        return self.title
# Create your models here.
