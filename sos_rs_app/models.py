from django.db import models
from uuid import uuid4

def up_picture_user(instance, filename):
    return f"{instance.id_user}-{filename}"

class Base(models.Model):
    created = models.DateField(auto_now_add=True)
    founded = models.BooleanField(default=False)
    missing_date = models.DateField(auto_now_add=False)

    class Meta:
        abstract = True


class User(Base):
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    picture = models.ImageField(upload_to=up_picture_user, blank=True, null=True)

    class Meta:
        verbose_name = 'User'


    def __str__(self) -> str:
        return self.name