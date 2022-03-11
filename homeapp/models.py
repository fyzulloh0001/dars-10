from audioop import reverse
from django.db import models
from django.urls import reverse

# Create your models here.

class Page(models.Model):
    title=models.CharField(max_length=150)
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    text=models.TextField()
    
    
    def get_absolute_url(self):
        return reverse('detailview', args=[str(self.pk)])
    

    
   