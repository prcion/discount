from django.db import models
from django.utils import timezone

class Discount(models.Model):

    img = models.ImageField(default='default.jpg', upload_to="post_image")
    title = models.CharField(max_length = 100)
    duration = models.PositiveIntegerField()
    pay = models.PositiveIntegerField()
    date = models.DateTimeField(default = timezone.now)
