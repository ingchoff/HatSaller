from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class hat(models.Model):
    title = models.CharField(max_length=30)
    stock = models.IntegerField(default=1)
    description = models.TextField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()

    def __str__(self):
        return "%s by %s" % (self.title, self.created_by)