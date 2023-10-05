from django.db import models

class Dialogue(models.Model):
    context = models.CharField(max_length=255)
    user_input = models.TextField()
    model_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
