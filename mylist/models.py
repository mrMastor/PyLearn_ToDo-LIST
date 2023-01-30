from django.db import models
from django.urls import reverse
from django.utils import timezone
import slugify
import random
import string


def random_string_generator(size=10, chars=string.ascii_lowercase):
    return "".join(random.choice(chars) for _ in range(size))


def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug
        unique_slug += random_string_generator(size=4)
    return unique_slug


class ToList(models.Model):

    status = models.BooleanField(default=False, help_text="Статус выполнения")
    name = models.CharField(max_length=64, verbose_name="Задача")
    slug = models.SlugField(
        null=False, unique=True, blank=True, db_index=True, verbose_name="URL Post"
    )
    date_complite = models.DateTimeField(
        auto_now=False, null=True, blank=True, default=None
    )
    date_create = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        """Переопределение сохранения."""
        if not self.slug:
            self.slug = unique_slugify(self, slugify.slugify(self.name))

        if self.status == True and self.date_complite == None:
            self.date_complite = timezone.now()
        if self.status == False:
            self.date_complite = None
        super(ToList, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("item_detail", args=[str(self.slug)])

    def __str__(self):
        """переопределение строкового представления объекта."""
        return f"{self.id} -> {self.name}"
