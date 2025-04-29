from django.db import models

# Create your models here.
class Book(models.Model):
    image = models.ImageField(upload_to='books/images/')
    STATUS_CHOCIES = [
        ('onrent','ติดเช่า'),
        ('free','ว่างให้เช่า')
    ]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    date = models.DateField()


    def __str__(self):
        return f"{self.name}, {self.price} บาท, หมวด: {self.category}, สถานะ: {self.status}"
        