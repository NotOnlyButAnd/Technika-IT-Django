from django.db import models

class Image(models.Model):
    image_id = models.IntegerField(primary_key=True)
    url = models.URLField()
    alt = models.CharField(max_length=100)

    class Meta:
        ordering = ["-image_id"]

    def __str__(self):
        return str(self.image_id)
