from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=255, unique=True)
    born_date = models.CharField(max_length=100)
    born_location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.fullname

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')
    tags = models.CharField(max_length=500) # Зберігатимемо як рядок або через ManyToMany

    def __str__(self):
        return self.quote[:50]