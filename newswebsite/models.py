from django.db import models
CATEGORY_CHOICES = [
        ('national','National'),
        ('politics','Politics'),
        ('valley','Valley'),
        ('opinion','Opinion'),
        ('money','Money'),
        ('sports','Sports'),
        ('culture','Culture'),
        ('others','Others')
    ]

class Post(models.Model):
    heading = models.CharField(max_length=255)
    image = models.URLField(blank=True)
    content = models.TextField(max_length=1000)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    url = models.URLField(max_length=255, null=True)




    def __str__(self):
        return self.heading

