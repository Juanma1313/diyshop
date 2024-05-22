from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import RowNumber
import time

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

STATUS = ((0, "Draft"), (1, "Published"))


class Thing(models.Model):
    '''Django database model for a Thing or a Component of the diy things '''

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='components')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    featured_image_url = models.URLField(max_length=1024, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='noimage.png')
    description = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='thing_likes', blank=True)
    variants = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'DIY Project'
        verbose_name_plural = 'DIY Projects'
        ordering = ["created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Instructions(models.Model):
    '''Django database model for Instructions of the diy things '''

    thing = models.ForeignKey(Thing, on_delete=models.CASCADE, related_name="instructions")

    def default_Instruction_title():
        now = time.localtime()
        return f"I-{now.tm_year}-{now.tm_mon}-{now.tm_mday}_{now.tm_hour}:{now.tm_min}:{now.tm_sec}"
    title = models.CharField(max_length=200, default=default_Instruction_title)
    instructions = models.TextField(blank=True, null=False)

    class Meta:
        verbose_name_plural = 'Instructions'
        ordering = ["title"]

    def __str__(self):
        return str(self.title)

