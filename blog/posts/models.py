from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()

class Tag(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=50) # kısa metinler için CharField kullanılır, max_length parametresi zorunludur
    content = models.TextField() # daha uzun metinler için TextField kullanılır
    created = models.DateTimeField(auto_now_add=True) # otomatik olarak oluşturulma tarihini ekler.
    updated = models.DateTimeField(auto_now=True) # her kaydedildiğinde güncellenme tarihini ekler.
    is_published = models.BooleanField(default=False) # varsayılan olarak False, yani yayınlanmamış olarak başlar.
    
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # bir postun sadece bir yazarı olabilir, on_delete=models.CASCADE ile yazar silindiğinde ilgili postların da silinmesini sağlıyoruz.
    tags = models.ManyToManyField(Tag, blank=True) # bir postun birden fazla tagi olabilir, blank=True ile boş bırakılabilir hale getiriyoruz.

