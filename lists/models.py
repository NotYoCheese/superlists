from django.db import models
from django.core.urlresolvers import reverse

class List(models.Model):

    def get_absolute_url(self):
        #generates the url based on the name mapped in urs.py
        return reverse('view_list', args=[self.id])

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
