from django.db import models

# Create your models here.
class userclient(models.Model):
    name=models.CharField(max_length=25)
    phone=models.CharField(max_length=16)
    email=models.EmailField()
    password=models.CharField(max_length=16)
    
    def __str__(self):
        return self.email
class user_query(models.Model):
    # user=models.ForeignKey(userclient,on_delete=models.CASCADE)
    Q_email=models.EmailField()
    query=models.CharField(max_length=200)

class adminuser(models.Model):
    name=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=16)
    suggestion=models.TextField(null=True)
    
    def __str__(self):
        return self.username

