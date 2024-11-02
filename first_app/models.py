from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def is_new_release(self):
        from datetime import date
        # Consider the book new if it was published within the last year.
        return (date.today() - self.published_date).days <= 365 * 10
    

class LibraryMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    membership_start = models.DateField()  # Date when the member joined the library
    email = models.EmailField()  # Email field with built-in validation
    books_borrowed = models.IntegerField(default=0)  # Number of books borrowed (default is 0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
