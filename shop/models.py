from django.db import models

from capybara_forms.models import CapybaraFormsCategory, CapybaraFormsModel


class Category(CapybaraFormsCategory):
    title = models.CharField(
        max_length=100)

    def __str__(self):
        return self.title


class Advert(CapybaraFormsModel(Category)):
    title = models.CharField(
        max_length=100)
    price = models.PositiveSmallIntegerField()
