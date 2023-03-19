from django.db import models


# Create your models here.
class CePost(models.Model):
    title= models.CharField(max_length=300, unique=True)
    date= models.DateField(null=True)
    time= models.TimeField(unique=True,null=True,blank=True) 
    img = models.ImageField(upload_to = 'img/krce/%m-%y',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField('Approved',default=False)
    def __str__(self):
        return self.title