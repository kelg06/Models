from django.db import models

# Create your models here.
class Library(models.Model):
    title = models.TextField()
    author = models.TextField()
    is_checked_out=models.BooleanField(default=False)
    is_favorite = models.BooleanField()


def checkout_book(title,author,is_favorite,is_checked_out=True):
    b=Library(title=title,author=author,is_favorite=is_favorite,is_checked_out=is_checked_out)
    b.save()
    return b
def all_books():
    return Library.objects.all()

def find_book_by_title(title):
    try:
        return Library.objects.get(title=title)
    except:
        return None

def favorite_book():
    return Library.objects.filter(is_favorite=True)

def update_book_author(title, new_author):
    return Library.objects.filter(title=title).update(author=new_author)

def delete_book(title):
    return Library.objects.get(title=title).delete()





