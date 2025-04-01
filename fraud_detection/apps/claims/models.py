from django.db import models
from django.contrib.auth import get_user_model

class InsuranceClaim(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.FloatField()
    is_fraudulent = models.BooleanField(default=False)
