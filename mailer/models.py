from django.db import models

# Create your models here.
class Contact(models.Model):
    sender_email = models.EmailField(max_length=122)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.sender_email
