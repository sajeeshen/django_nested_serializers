from core.models import Author
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.slug import generate_unique_slug


@receiver(post_save, sender=Author)
def create_author_slug(sender, instance, created, **kwargs):
    """ Create author slug based on the author name """
    if created:
        slug = generate_unique_slug(Author, instance.name)
        instance.slug = slug
        instance.save()