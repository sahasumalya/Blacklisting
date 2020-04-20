from django.db import models

class Ipv4(models.Model):
    ip = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.ip
