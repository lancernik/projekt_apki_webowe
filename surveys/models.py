from django.db import models

# Create your models here.




class Survey(models.Model):
    sample_text = models.CharField(max_length=1024, blank=True, null=True)
    sample_bool = models.BooleanField(blank=True, null=True, default=False)

