from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):#post na blogu
    author = models.ForeignKey('auth.User')#klasa post dziedziczy po klasie models
    title = models.CharField(max_length=200)# to są właściwości klasy(definicje kolumn)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):# self -tzn. konkretny artykuł do opublikowania, odwołanie do biezącego obiektu
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#__ mówi, że jeśli wykonamy str z argumentem naszej klasy, to ma użyć tytułu artykułu
        return self.title