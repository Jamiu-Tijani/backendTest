from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your models here.
class userData(User):
    fields = ['username','password','email']
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    def __str__(self):
        return self.username

    def email_user(email, subject, message, from_email, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [email], **kwargs)
    
    
    def imageURL(self):
        try:
            url = self.avatar.url
        except:
            url = ''
        return url

    