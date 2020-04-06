from django.db import models

class Place(models.Model):
    title=models.CharField(max_length=120)
    body=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2,default=29.99)
    image=models.FileField(upload_to='places/images/',null=True)
    image2=models.FileField(upload_to='places/images/',null=True)
    slug=models.SlugField(unique=True)
    time=models.DateTimeField(auto_now_add=True, auto_now=False)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title