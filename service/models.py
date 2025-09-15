from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/')
    lp_url = models.URLField('LPリンク', blank=True)

    def __str__(self):
        return self.name