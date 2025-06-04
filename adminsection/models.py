from django.db import models

# Create your models here.
class Program(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

