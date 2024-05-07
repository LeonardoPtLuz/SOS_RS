from django.db import models


class Base(models.Model):
    created = models.DateField(auto_now_add=True)
    founded = models.BooleanField(default=False)
    missing_date = models.DateField(auto_now_add=False)

    class Meta:
        abstract = True


class User(Base):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    class Meta:
        verbose_name = 'User'


    def __str__(self) -> str:
        return self.name