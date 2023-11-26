from django.db import models
class PublishingHouse(models.Model):
    name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} - {self.contact_number} - {self.location}"
class Author(models.Model):
    publiszing = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    birth_year = models.DateField()

    def __str__(self):
        return f"{self.pk} - {self.first_name} - {self.alias} - {self.last_name} - {self.publiszing} - {self.birth_year}"


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.pk} - {self.title}  {self.price}. Author id = {self.author}"
