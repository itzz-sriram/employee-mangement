from django.db import models

# Create your models here.
class usr_profile(models.Model):
    usr_id = models.IntegerField(null=False,blank=False,unique=False)
    usr_name = models.CharField(null=False,max_length=30)
    usr_gender = models.CharField(null=False,max_length=6)
    usr_mobile = models.BigIntegerField()
    usr_email = models.EmailField()
    usr_education = models.CharField(max_length=10)
    usr_skill = models.CharField(max_length=50)
    usr_address = models.CharField(max_length=30,null=True)




    def __str__(self):
        return '%s'%(self.usr_id)