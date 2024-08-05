from django.db import models

class Footer(models.Model):
    addre = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=17)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)


class Form(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subjects = models.CharField(max_length=60)
    body = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subjects}"