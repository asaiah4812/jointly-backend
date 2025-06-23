from django.db import models
import uuid

# Create your models here.

class Email(models.Model):
    id = models.CharField(primary_key=True,unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username