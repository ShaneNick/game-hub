from django.db import models

class Player(models.Model):
    username = models.CharField(max_length = 35)
    email_address = models.EmailField(max_length = 254)
    password =  models.password(max_length = 20)

