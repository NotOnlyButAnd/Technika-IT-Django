import graphene
from django.conf import settings
from graphene_django import DjangoObjectType

from client_app import models


class ImageType(DjangoObjectType):
    class Meta:
        model = models.Image


class Query(graphene.ObjectType):
    all_images = graphene.List(ImageType)
    post_by_url = graphene.Field(ImageType, url=graphene.String())
    posts_by_alt = graphene.List(ImageType, alt=graphene.String())
    
    def resolve_all_images(root, info):
        return (
            models.Image.objects.all()
        )

    def resolve_image_by_url(root, info, url):
        return (
            models.Image.objects.get(url=url)
        )

    def resolve_image_by_alt(root, info, alt):
        return (
            models.Image.objects.get(alt=alt)
        )


schema = graphene.Schema(query=Query)
