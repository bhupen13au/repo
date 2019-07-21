from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=30)
    authour_name = models.CharField(max_length=30)
    book_price = models.IntegerField()
    book_code = models.IntegerField()

    class Meta:
        db_table="book_details"