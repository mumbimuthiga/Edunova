from django.db import models
from django.conf import settings

# Create your models here.
class Programs(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'adminsection_program' 
