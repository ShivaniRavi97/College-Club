from django.db import models



class events(models.Model):
    parname = models.ForeignKey('parname.User', on_delete=models.CASCADE)
    

    
    def __str__(self):
        return self.title