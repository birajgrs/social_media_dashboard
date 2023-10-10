from django.db import models

class Tweet(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField()
    user = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.user} {self.text}"

class FacebookPost(models.Model):
    message = models.TextField()
    created_time = models.DateTimeField()
    user_id = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user_id} {self.message}"
