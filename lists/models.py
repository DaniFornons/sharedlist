import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shopping_lists"
    )
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Item(models.Model):
    shopping_list = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="items"
    )
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=50, blank=True)
    done = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["done", "name"]

    def __str__(self):
        return self.name

def generate_uuid_hex():
    return uuid.uuid4().hex

