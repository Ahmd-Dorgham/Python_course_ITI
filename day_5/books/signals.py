from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book
from .models import ISBN

@receiver(post_save, sender=Book)
def create_book_isbn(sender, instance, created, **kwargs):
    if created == True:
        if instance.user != None:
            my_author = instance.user.username
        else:
            my_author = "No author found"
            
        ISBN.objects.create(
            book=instance,
            book_title=instance.title,
            author_title=my_author
        )
