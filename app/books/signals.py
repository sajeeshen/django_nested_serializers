from core.models import Book
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.slug import generate_unique_slug


@receiver(post_save, sender=Book)
def create_book_slug(sender, instance, created, **kwargs):
    """ Create slug for Books based on the book name """
    if created:
        slug = generate_unique_slug(Book, instance.name)
        instance.slug = slug
        instance.save()